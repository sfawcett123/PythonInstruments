from instrument import instrument , component_types
import pygame

class Altimeter( instrument.Instrument ):
    _height = 0
    _qnh = 0
    _power = False

    def __init__( self , **kwargs ):
        super().__init__(
             window = True,
             # size= (300,300),
             components = [ { "img": "../content/altimeter.png"                                                    , "type": component_types.ComponentType.FACE},
                            { "name": "flag"    , "img": "../content/stby_flag.png" , "scale": .75 ,  "location": (135,140)            , "type": component_types.ComponentType.FLAG},
                            { "name": "mask"    , "location": (120,120) , "layer": -6 ,"height": 50, "width": 100  , "type": component_types.ComponentType.MASK },
                            { "name": "h_100"   , "scale": 0.8  , "location": (160,230) , "magnitude":1            , "type": component_types.ComponentType.COUNTER },
                            { "name": "h_1000"  , "scale": 1.8  , "location": (80 ,220) , "magnitude":2            , "type": component_types.ComponentType.COUNTER },
                            { "name": "qnh"     , "scale": 0.75 , "location": (310,315) , "magnitude":4            , "type": component_types.ComponentType.COUNTER },
                            { "name": "height"  , "max": 100 , "img": "../content/LongPointer.bmp"              , "type": component_types.ComponentType.POINTER},
                          ] )
        self.height = kwargs.get( "height" , 0  )
        self.qnh    = kwargs.get( "qnh"    , 1000)
        self.power  = kwargs.get( "power"  , False )

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
        h_100 = self._height // 100 % 10 * 100
        h_1000 = self._height // 1000 % 10
        self.update( "h_100"  , h_100 )
        self.update( "h_1000" , h_1000 )
        self.update( "height" , value )

    @property
    def qnh(self):
        return self._qnh

    @qnh.setter
    def qnh( self, value):
        self._qnh = value
        self.update( "qnh" , value )

    @property
    def power(self):
        return self._power

    @power.setter
    def power( self, value ):
        self._power = value
        self.update( "flag" , value )
