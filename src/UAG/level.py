from random import choice
import pygame
from weapon import Weapon
from settings import *
from tile import Tile
from player import Player
from debug import debug
from ui import UI
from utility import import_csv_layout, import_folder

class Level():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        # Sprite groups
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # Attack sprites
        self.current_attack = None

        # Map generation
        self.create_map()

        # UI
        self.ui = UI()

    def create_map(self):
        layouts = {
            'boundary': import_csv_layout('levels/0/overworld_Boundary.csv'),
            'grass': import_csv_layout('levels/0/overworld_Grass.csv'),
            'objects': import_csv_layout('levels/0/overworld_Objects.csv')
        }

        graphics = {
            'grass': import_folder('graphics/grass'),
            'objects': import_folder('graphics/objects')
        }

        for style,layout in layouts.items():
            for row_index,row in enumerate(layout):
                for col_index,col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x,y),[self.obstacle_sprites],'invisible')
                        if style == 'grass':
                            random_grass_image = choice(graphics['grass'])
                            Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'grass',random_grass_image)
                        if style == 'objects':
                            object_surf = graphics['objects'][int(col)]
                            Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'object',object_surf)

        self.player = Player(
            (3000,3000),
            [self.visible_sprites],
            self.obstacle_sprites,
            self.create_attack,self.destroy_attack,
            self.create_magic,self.destroy_magic)

    def create_attack(self):
        self.current_attack = Weapon(self.player,[self.visible_sprites])

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def create_magic(self,style,strength,cost):
        print(style)
        print(strength)
        print(cost)

    def destroy_magic(self):
        pass

    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.ui.display(self.player)

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        self.floor_surf = pygame.image.load('graphics/tilemaps/overworld.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

    def custom_draw(self,player):
        # Player offset for center camera
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf,floor_offset_pos)

        #for sprite in self.sprites():
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_position = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_position)