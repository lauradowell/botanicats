
import pygame
from settings import tile_size
from tiles import Tile
from player import  Player, Player2



class Level:
    #level setup
    def __init__(self, level_data, surface):

        self.display_surface = surface
        self.setup_level (level_data)

        self.world_shift = 0
    
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'X':
                    tile = Tile((x,y), tile_size)
                    self.tiles.add(tile)
                
                if cell == 'P' :
                    player_one = Player((x,y))
                    self.player.add(player_one)
                
                if cell == 'D' :
                    player_two = Player2((x,y))
                    self.player.add(player_two)

                
   
    def run(self):

        #tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
         
        #players
        self.player.update()
        self.player.draw(self.display_surface)

        