import math
import random
import time


class Animal:
    def __init__(self, coordinates, foodCoordinates, waterCoordinates, speed):
        self.hungry = 100
        self.thirst = 100
        self.breed = 100
        self.need = 0
        self.speed = speed  # 5 координат в тик
        self.coordinates = coordinates
        self.foodCoordinates = foodCoordinates
        self.waterCoordinates = waterCoordinates
        self.nowTick = 0

    def everyTick(self):
        self.nowTick += 1
        self.hungry -= 1
        self.thirst -= 1
        # print(self.nowTick)
        self.breed -= 0.25

    def detectNeed(self):
        if self.thirst and self.hungry > 99:
            self.need = 2
        elif self.thirst < self.hungry or self.hungry > 99:
            self.need = 0
        elif self.hungry < self.thirst or self.thirst > 99:
            self.need = 1

    def vision(self, targetCoordinates: list[int]) -> list[int]:
        distanceToTarget = round(math.sqrt(abs(self.coordinates[0] - targetCoordinates[0]) ** 2 + abs(
            self.coordinates[1] - targetCoordinates[1]) ** 2))
        return distanceToTarget

    def move(self, targetCoordinates: list[int]):
        distance = self.vision(targetCoordinates)
        self.nowTick += round(distance / self.speed)
        for i in range(round(distance / self.speed)):
            self.everyTick()
        self.coordinates = targetCoordinates
        # print(coordinates)

    def walk(self):
        coords = [random.randint(self.coordinates[0] - self.speed, self.coordinates[0] + self.speed),
                  random.randint(self.coordinates[1] - self.speed, self.coordinates[1] + self.speed)]
        self.move(coords)

    def distance(self, Coordinates: list[int]):
        k = 0
        a = []
        distances = []
        closeTargets = []
        for i, r in zip(Coordinates[::2], Coordinates[1::2]):
            a.append(i)
            a.append(r)
            distanceToTarget = self.vision(a)
            if distanceToTarget < 50:
                closeTargets.append(a[k])
                closeTargets.append(a[k + 1])
                distances.append(distanceToTarget)
            k += 2
            return distances, a, closeTargets

    def goFood(self):
        distances, a, closeFood = self.distance(self.foodCoordinates)
        i = 0
        if distances:
            minIndex = distances.index(min(distances))
            a.clear()
            a.append(closeFood[minIndex + minIndex])
            a.append(closeFood[minIndex + minIndex + 1])
            self.move(a)
            if self.hungry + 5 > 100: self.hungry += 100 - self.hungry
            else: self.hungry += 5

            # print(f"Hungry {self.hungry}")
        else:
            while i == 0:
                distances, a, closeFood = self.distance(self.foodCoordinates)
                if distances: i = 1
                self.walk()
                # print(1)
            if self.hungry + 5 > 100: self.hungry += 100 - self.hungry
            else: self.hungry += 5
            # print(self.hungry)

    def goDrink(self):
        distances, a, closeWater = self.distance(self.waterCoordinates)
        i = 0
        if distances:
            minIndex = distances.index(min(distances))
            a.clear()
            a.append(closeWater[minIndex + minIndex])
            a.append(closeWater[minIndex + minIndex + 1])
            self.move(a)
            if self.thirst + 5 > 100: self.thirst += 100 - self.thirst
            else: self.thirst += 5

            # print(f"Hungry {self.hungry}")
        else:
            while i == 0:
                distances, a, closeWater = self.distance(self.foodCoordinates)
                if distances: i = 1
                self.walk()
                # print(1)
            if self.thirst + 5 > 100: self.thirst += 100 - self.thirst
            else: self.thirst += 5
            print(self.thirst)

    def goBreed(self):
        pass

    def main(self):
        self.everyTick()
        self.detectNeed()
        if self.need == 0:
            self.goDrink()
            # print(0)
        elif self.need == 1:
            self.goFood()
            # print(1)
        else:
            self.goBreed()
            # print(2)
        print("Simulation Agents 1.3.6V")
        print(f"Hungry - {self.hungry}")
        print(f"Thirst - {self.thirst}")
        print(f"Now tick - {self.nowTick}")
        print(f"Coordinates - {self.coordinates}")
        print(f"Food coordinates - {self.foodCoordinates}")
        print("___________________________")
        time.sleep(1)
