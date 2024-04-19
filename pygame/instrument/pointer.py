from .image import image
import pygame

class Pointer( image.Image ):
    def __init__( self, screen, image, **kwargs ):
        super().__init__( screen , image , **kwargs )

    def blit( self ):
        """Override blit to rotate around centre with value as an angle"""
        w , h = self.img.get_size()
        h = h - 40 # adjust for pointer height
        w = w/2    # adjust for pointer width
        img , pos = self.rotate_center( w, h )
        self.screen.blit( img , pos )
        self.display = self.value