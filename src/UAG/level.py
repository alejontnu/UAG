import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from utility import import_csv_layout, import_folder

class Level():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        layouts = {
            'collision': import_csv_layout('levels/0/area_1._collision.csv'),
            'flora': import_csv_layout('levels/0/area_1._flora.csv'),
            'ground': import_csv_layout('levels/0/area_1._ground.cvs')
        }

        graphics = {
            'grass': import_folder('graphics/sprites')
        }
        for style,layout in layouts.items():
            for row_index,row in enumerate(WORLD_MAP):
                for col_index,col in enumerate(row):
                    if col != -1:
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'collisions':
                            Tile((x,y),[self.obstacle_sprites],'invisible')
                        if style == 'fauna':
                            pass
                        if style == 'object':
                            pass
    #             if col == 'x':
    #                 Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
    #             if col == 'p':
    #                 self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)
        self.player = Player((2000,600),[self.visible_sprites],self.obstacle_sprites)

    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        self.floor_surf = pygame.image.load('graphics/tilemaps/area_1.png').convert()
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