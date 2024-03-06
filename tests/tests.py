from main.base_agent import Animal

testAgent = Animal([10, 10], [20, 20], [20, 20], 5)
test_coordinates = [20, 20]


def testVision():
    assert testAgent.vision(test_coordinates) == 14


def testMove():
    testAgent.move(test_coordinates)
    assert testAgent.coordinates == test_coordinates


def testDistance():
    distance, a, closeTargets = testAgent.distance(test_coordinates)
    assert distance == [14]
    assert a == [20, 20]
    assert closeTargets == [20, 20]


def testGoFood():
    testAgent.goFood()
    assert testAgent.coordinates == [20, 20]


def testGoWater():
    testAgent.goDrink()
    assert testAgent.coordinates == [20, 20]
