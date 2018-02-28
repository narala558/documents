import time

import pygame.image
from pygame import camera



for i in range(1000):
    camera.init()
    cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
    cam.start()
    img = cam.get_image()
    time.sleep(1)
    name = '{}.bmp'.format(i)
    pygame.image.save(img, name)

pygame.camera.quit()
