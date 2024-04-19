from .image import image

class Face( image.Image ):

    def __init__( self, screen, image, **kwargs ):
        super().__init__( screen , image , **kwargs )