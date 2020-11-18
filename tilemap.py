
import pygame
import pytmx 

class TileMap:
    def __init__(self, filename):
        tilemap = pytmx.load_pygame(filename, pixealpha=True)
        self.width  = tilemap.width  * tilemap.tilewidth
        self.height = tilemap.height * tilemap.tileheight
        self.tmxdata = tilemap
    
    def render(self, surf):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        surf.blit(tile, (x * self.tmxdata.tilewidth, y * self.tmxdata.tileheight))
    
    def make_map(self):
        temp_surf = pygame.Surface((self.width, self.height))
        self.render(temp_surf)
        return temp_surf