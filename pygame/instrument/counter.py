from .image import image
import pygame

class Counter( image.Image ):

    magnitude = 5    # The number of digits in the counter

    def __init__( self, screen, **kwargs ):
        self.magnitude = kwargs.get( "magnitude" , 5 )
        super().__init__( screen , "../content/numbers.png" , **kwargs )

    def convert( self  ):
        return [int(d) for d in str(self.value).zfill(self.magnitude)]

    def rotate( self , digit):
        x = self.convert()
        offset = 0 - ( self.img.get_height() / 12 ) # 12 digits needed to make it look wrapped
        return  self.location[1] + ( offset * ( x[ digit ] + 1) ) # add one as counter starts at

    def column( self , digit , padding=0 ):
        width = ( self.img.get_width() ) + padding
        return self.location[0] + ( digit * width )

    def blit( self ):
        """Override blit to rotate around centre with value as an angle"""
        for d in range(0,self.magnitude ):
           self.screen.blit( self.img , pygame.Rect( self.column( d ) , self.rotate( d ) , 100,100 ) )

        self.display = self.value