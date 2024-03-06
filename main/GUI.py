import pygame
import sys

BLACK = (2, 1, 18)
WHITE = (255, 255, 255)
GREEN = (0, 100, 0)
BLUE = (0, 191, 255)

sc = pygame.display.set_mode((600, 600))

animalObject = pygame.Surface((10, 10))
animalObject.fill(WHITE)
food = pygame.Surface((15, 15))
food.fill(GREEN)
water = pygame.Surface((15, 15))
water.fill(BLUE)

rectAnimal = animalObject.get_rect()
rectFood = food.get_rect()
rectWater = water.get_rect()


# TODO: Добавить возможность создавать объект источников воды и еды.
