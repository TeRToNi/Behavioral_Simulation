from base_agent import Animal
from GUI import *
import random
import time

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


def main():
    animal.everyTick()
    animal.detectNeed()
    if animal.need == 0:
        animal.goDrink()
    elif animal.need == 1:
        animal.goFood()
    else:
        animal.goBreed()
    print(animal)
    time.sleep(1)


running = True
while running:
    main()
    coordinates.append(coordinates)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    sc.fill(GREEN)
    sc.blit(surf, rect)
    pygame.display.update()

    rect.x = animal.coordinates[0]
    rect.y = animal.coordinates[1]
