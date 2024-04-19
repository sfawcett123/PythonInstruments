import pygame
from ..helpers.colours import Colours


class Image:
    layer = 0 # the order to draw the stacked layers
    name = "" # give the layer a name, this way we can find it easier to set a value, names do not have to be unique
    value = 0 # value, this can mean anything depending on the update
    display = -1
    location = (0,0) # When on the dial the rectangle should display
    center = False
    img = None

    def __init__( self, screen, image,  **kwargs ):
        self.screen = screen
        if image:
            img = pygame.image.load( image ).convert()
            img.set_colorkey( Colours.TRANSPARANT )
        else:
            img = None

        self.name   = kwargs.get("name"  , image )
        print( f"Initialising {self.name}")
        self.ratio  = kwargs.get("ratio" , 0.0 )
        self.layer  = kwargs.get("layer" , 0)
        self.scale  = kwargs.get("scale" , 0)
        self.center = kwargs.get("centre", False)

        if kwargs.get("location"):
            self.location = kwargs["location"]

        if img:
            if kwargs.get("size"):
                self.img = pygame.transform.smoothscale(img, kwargs.get("size") )
            elif self.scale > 0:
                r = img.get_size()
                x = r[0] * self.scale
                y = r[1] * self.scale
                self.img = pygame.transform.smoothscale(img, ( x, y ) )
            else:
                self.img = img

    def centre( self ):
        """get the centre of the image in relation to the centre of the screen"""
        return self.img.get_rect(center = self.screen.get_rect().center)

    def update( self, value ):
        """set the value of the instrument, override if you need to convert"""
        self.value = value

    def blit( self ):
        """draw the image how it is, override if you want to rotate"""

        if self.center:
            local_rect = self.centre()
        else:
            local_rect = self.img.get_rect()

        self.screen.blit( self.img , local_rect )

    def angle( self ):
        """adjust the angle to the ratio of the max value / 360"""
        return -self.value * self.ratio

    def rotate_center(self , w=0, h=0 ):
        """rotate an image while keeping its center and size"""
        pos = (self.screen.get_width()/2, self.screen.get_height()/2)
        originPos = (w,h)

        image_rect = self.img.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
        offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

        rotated_offset = offset_center_to_pivot.rotate(-self.angle())
        rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
        rotated_image = pygame.transform.rotate(self.img, self.angle())
        rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

        return rotated_image , rotated_image_rect

    def __repr__(self):
        return( self.name )

    def __str__(self):
        return( self.name )