from instrument import instrument , component_types
import pygame

class Altimeter( instrument.Instrument ):
    def __init__( self ):
        super().__init__( [ { "img": "../content/altimeter.png"                                                    , "type": component_types.ComponentType.FACE},
                            { "name": "flag"    , "img": "../content/stby_flag.png" , "scale": .75 ,  "location": (135,140)            , "type": component_types.ComponentType.FLAG},
                            { "name": "mask"    , "location": (120,120) , "layer": -6 ,"height": 50, "width": 100  , "type": component_types.ComponentType.MASK },
                            { "name": "h_100"   , "scale": 0.8  , "location": (160,230) , "magnitude":1            , "type": component_types.ComponentType.COUNTER },
                            { "name": "h_1000"  , "scale": 1.8  , "location": (80 ,220) , "magnitude":2            , "type": component_types.ComponentType.COUNTER },
                            { "name": "qnh"     , "scale": 0.75 , "location": (310,315) , "magnitude":4            , "type": component_types.ComponentType.COUNTER },
                            { "name": "height"  , "ratio": 0.35 , "img": "../content/LongPointer.bmp"              , "type": component_types.ComponentType.POINTER},
                          ] )

    def height( self, value: int) -> None:
        h_100 = value // 100 % 10 * 100
        h_1000 = value // 1000 % 10
        self.update( "h_100" , h_100 )
        self.update( "h_1000" , h_1000 )
        self.update( "height" , value )
        self.blit()
        pygame.display.update()

    def qnh( self, value: int) -> None:
        self.update( "qnh" , value )
        self.blit()
        pygame.display.update()

    def flag( self, value: bool ) -> None:
        self.update( "flag" , value )
        self.blit()
        pygame.display.update()
