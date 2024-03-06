from base_agent import Animal
import random
from GUI import *

pastCoordinates = []
coordinates = [10, 20, 0, 0]
foodCoordinates = [coordinates[0] + random.randint(-20, 20),
                   coordinates[1] + random.randint(-20, 20)]
waterCoordinates = [coordinates[0] + random.randint(-20, 20),
                    coordinates[1] + random.randint(-20, 20)]

animal = Animal(coordinates, foodCoordinates, waterCoordinates, 5)

running = True
while running:
    animal.main()
    coordinates.append(coordinates)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = not running
    clock.tick(FPS)
    all_sprites.update(coordinates[0], coordinates[1])

    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()
    animal.waterCoordinates.append(animal.coordinates[0] + random.randint(-20, 20))
    animal.waterCoordinates.append(animal.coordinates[1] + random.randint(-20, 20))
    animal.foodCoordinates.append(animal.coordinates[0] + random.randint(-20, 20))
    animal.foodCoordinates.append(animal.coordinates[1] + random.randint(-20, 20))
