from .image import image
from .helpers.colours import Colours
import pygame

class Flag( image.Image ):

    mask_image = None

    def blit( self ):
        """Override blit to rotate around centre with value as an angle"""
        if not self.mask_image:
            r = self.img.get_rect()
            self.mask_img = pygame.Surface( ( r.width , r.height ))
            self.mask_img.fill( Colours.BACKGROUND )

        if self.value:
            self.screen.blit( self.img ,  (self.location[0] , self.location[ 1 ] , 100,100 ) )
        else:
            self.screen.blit( self.mask_img ,  (self.location[0] , self.location[ 1 ] , 100,100 ) )

        self.display = self.value