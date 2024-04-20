import os
import pygame
from .component_types import ComponentType
from .face import Face
from .flag import Flag
from .dial import Dial
from .counter import Counter
from .pointer import Pointer
from .mask import Mask
from .helpers.dict2obj import Dict2Obj

class Instrument:
    images = []

    def __init__( self , **kwargs):

        size = kwargs.get( "size" , (460,460)  )
        position = kwargs.get( "position" , (0,0)  )
        components = kwargs.get( "components"   )
        window = kwargs.get( "window" , True   )

        if not window:
            FLAGS = pygame.NOFRAME
        else:
            FLAGS = 0

        pygame.init()
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % position
        self.screen = pygame.display.set_mode( size  , FLAGS)

        for c in components:
            component = Dict2Obj( c )
            if component.type == ComponentType.FACE:
                 f = Face( self.screen, component.img , size=size , centre=True, layer=0)
                 self.images.append( f )

            if component.type == ComponentType.FLAG:
                 f = Flag( self.screen, component.img , name=component.name , location=component.location, scale=component.scale , layer=-5)
                 self.images.append( f )

            if component.type == ComponentType.DIAL:
                 f = Dial( self.screen, component.img , size=size , centre=True , layer= -10 , name=component.name )
                 self.images.append( f )

            if component.type == ComponentType.COUNTER:
                f = Counter( self.screen,  location=component.location,
                                           layer= -15 ,
                                           scale=component.scale ,
                                           name=component.name,
                                           magnitude=component.magnitude )
                self.images.append( f )

            if component.type == ComponentType.POINTER:
                 f = Pointer( self.screen, component.img , max=component.max, centre=True , layer=5 , name=component.name )
                 self.images.append( f )

            if component.type == ComponentType.MASK:
                 f = Mask( self.screen, layer=component.layer ,location=component.location , height=component.height, width=component.width )
                 self.images.append( f )

    def update( self , name , value):
        for control in [ x for x in self.images if x.name == name ]:
            control.update( value )
        self.blit()

    def blit( self ):
        for i in sorted( self.images, key=lambda img: img.layer):
            i.blit()
        pygame.display.update()
