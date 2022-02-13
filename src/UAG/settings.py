# game setup
WIDTH    = 1280 
HEIGTH   = 720
FPS      = 60
TILESIZE = 64

# UI stuff 
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = 'graphics/font/Pixellettersfull.ttf'
UI_FONT_SIZE = 18
 
# general colours
WATER_COLOUR = '#71ddee'
UI_BG_COLOUR = '#222222'
UI_BORDER_COLOUR = '#111111'
TEXT_COLOUR = '#EEEEEE'
 
# ui colours
HEALTH_COLOUR = 'red'
ENERGY_COLOUR = 'blue'
UI_BORDER_COLOUR_ACTIVE = 'gold'
 
# upgrade menu
TEXT_COLOUR_SELECTED = '#111111'
BAR_COLOUR = '#EEEEEE'
BAR_COLOUR_SELECTED = '#111111'
UPGRADE_BG_COLOUR_SELECTED = '#EEEEEE'

# weapons 
weapon_data = {
    'sword': {'cooldown': 100, 'damage': 15,'graphic':'graphics/weapons/sword/full.png'},
    #'lance': {'cooldown': 200, 'damage': 25,'graphic':'graphics/weapons/lance/full.png'},
    #'spear': {'cooldown': 200, 'damage': 20,'graphic':'graphics/weapons/spear/full.png'},
    #'axe': {'cooldown': 400, 'damage': 35, 'graphic':'graphics/weapons/axe/full.png'},
    'hammer':{'cooldown': 500, 'damage': 40, 'graphic':'graphics/weapons/hammer/full.png'}}

# magic
magic_data = {
    'flame': {'strength': 5,'cost': 20,'graphic':'graphics/particles/flame/fire.png'},
    'heal' : {'strength': 20,'cost': 10,'graphic':'graphics/particles/heal/heal.png'},
    'bind' : {'strength': 5,'cost': 10,'graphic':'graphics/particles/bind/bind.png'}}

NUMBER_WEAPONS = len(weapon_data)
NUMBER_SPELLS = len(magic_data)