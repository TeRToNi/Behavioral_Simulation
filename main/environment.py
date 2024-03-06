from base_agent import Animal
from GUI import *
import random

pastCoordinates = []
coordinates = [400, 400, 0, 0]
foodCoordinates = [coordinates[0] + random.randint(-20, 20),
                   coordinates[1] + random.randint(-20, 20),
                   coordinates[0] + random.randint(-20, 20),
                   coordinates[1] + random.randint(-20, 20)
                   ]
waterCoordinates = [coordinates[0] + random.randint(-20, 20),
                    coordinates[1] + random.randint(-20, 20),
                    coordinates[0] + random.randint(-20, 20),
                    coordinates[1] + random.randint(-20, 20)
                    ]

animal = Animal(coordinates, foodCoordinates, waterCoordinates, 5)

running = True
while running:
    animal.main()
    coordinates.append(coordinates)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    sc.fill(GREEN)
    sc.blit(surf, rect)
    pygame.display.update()

    rect.x = animal.coordinates[0]
    rect.y = animal.coordinates[1]

    #animal.waterCoordinates.append(animal.coordinates[0] + random.randint(-20, 20))
    #animal.waterCoordinates.append(animal.coordinates[1] + random.randint(-20, 20))
    #animal.foodCoordinates.append(animal.coordinates[0] + random.randint(-20, 20))
    #animal.foodCoordinates.append(animal.coordinates[1] + random.randint(-20, 20))
