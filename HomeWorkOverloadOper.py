class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

Build1 = Building(10, 'Жилой дом')
Build2 = Building(5, 'Административное здание')
print(Build1 == Build2)