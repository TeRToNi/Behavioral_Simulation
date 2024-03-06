from base_agent import Animal
from GUI import *
import random
import time

pastCoordinates = []
coordinates = [300, 300, 0, 0]
foodCoordinates = [coordinates[0] + random.randint(-50, 50),
                   coordinates[1] + random.randint(-50, 50),
                   # coordinates[0] + random.randint(-20, 20),
                   # coordinates[1] + random.randint(-20, 20)
                   ]
waterCoordinates = [coordinates[0] + random.randint(-50, 50),
                    coordinates[1] + random.randint(-50, 50),
                    # coordinates[0] + random.randint(-20, 20),
                    # coordinates[1] + random.randint(-20, 20)
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

    sc.fill(BLACK)
    sc.blit(food, rectFood)
    sc.blit(water, rectWater)
    sc.blit(animalObject, rectAnimal)
    pygame.display.update()

    rectAnimal.x = animal.coordinates[0]
    rectAnimal.y = animal.coordinates[1]
    rectFood.x = foodCoordinates[0]
    rectWater.x = waterCoordinates[0]
    rectFood.y = foodCoordinates[1]
    rectWater.y = waterCoordinates[1]
