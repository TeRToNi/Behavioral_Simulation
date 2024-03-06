import pygame
import sys

GREEN = (2, 1, 18)
WHITE = (255, 255, 255)

sc = pygame.display.set_mode((800, 800))

surf = pygame.Surface((10, 10))
surf.fill(WHITE)

rect = surf.get_rect()

# TODO: Добавить возможность создавать объект источников воды и еды.
