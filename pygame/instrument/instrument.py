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

    def __init__( self , components , size=(490,490) ):
        pygame.init()
        self.screen = pygame.display.set_mode( size  , pygame.NOFRAME )

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
                 f = Pointer( self.screen, component.img , ratio=component.ratio, centre=True , layer=5 , name=component.name )
                 self.images.append( f )

            if component.type == ComponentType.MASK:
                 f = Mask( self.screen, layer=component.layer ,location=component.location , height=component.height, width=component.width )
                 self.images.append( f )

    def update( self , name , value):
        for control in [ x for x in self.images if x.name == name ]:
            control.update( value )

    def blit( self ):
        for i in sorted( self.images, key=lambda img: img.layer):
            i.blit()
        pygame.display.update()
