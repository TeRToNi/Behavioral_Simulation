from base_agent import Animal
import random

pastCoordinates = []
coordinates = [10, 20, 0, 0]
foodCoordinates = [coordinates[0] + random.randint(-20, 20),
                   coordinates[1] + random.randint(-20, 20)]
waterCoordinates = [coordinates[0] + random.randint(-20, 20),
                    coordinates[1] + random.randint(-20, 20)]

animal = Animal(coordinates, foodCoordinates, waterCoordinates, 5)

while True:
    animal.main()
    coordinates.append(coordinates)
    animal.waterCoordinates.append(animal.coordinates[0] + random.randint(-20, 20))
    animal.waterCoordinates.append(animal.coordinates[1] + random.randint(-20, 20))
    animal.foodCoordinates.append(animal.coordinates[0] + random.randint(-20, 20))
    animal.foodCoordinates.append(animal.coordinates[1] + random.randint(-20, 20))
