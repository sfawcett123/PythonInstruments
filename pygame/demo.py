import pygame
from altimeter import Altimeter

altimeter = Altimeter( height=0 , qnh=1020 , power=False)

clock = pygame.time.Clock()

done = False
while not done:
   clock.tick(60)
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
           done = True
   altimeter.height += 1

   if altimeter.height < 1000:
      altimeter.power = False
   else:
      altimeter.power = True