from .image import image
import pygame
from .helpers.colours import Colours

class Mask( image.Image ):

    def __init__( self, screen,  **kwargs ):
        width = int( kwargs.get( "width" , 100 ) )
        height = int( kwargs.get( "height" , 100 ))
        self.img = pygame.Surface( ( width , height ))
        self.img.fill( Colours.BACKGROUND )
        super().__init__( screen , image=None , **kwargs )

    def blit( self ):
        """Override blit to rotate around centre with value as an angle"""
        self.screen.blit( self.img ,  (self.location[0] , self.location[ 1 ] , 100,100 ) )