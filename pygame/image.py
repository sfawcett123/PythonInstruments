import pygame
from altimeter import Altimeter

altimeter = Altimeter()
done = False

h = 0000

clock = pygame.time.Clock()

while not done:
   clock.tick(60)
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
           done = True
   h = h +1
   altimeter.height( h )
   altimeter.qnh( 2992 )

   if h < 1000:
      altimeter.flag( False )
   else:
      altimeter.flag( True )