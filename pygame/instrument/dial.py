from .image import image

class Dial( image.Image ):

    def __init__( self, screen, image, **kwargs ):
        super().__init__( screen , image , **kwargs )

    def blit( self ):
        """Override blit to rotate around centre with value as an angle"""
        img = self.rotate_center()
        self.screen.blit( img , self.screen.get_rect() )

    def update( self, value ):
        super().update( value - 180 + 28.1)
