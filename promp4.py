class FavoriteAnimal:
    def __init__(self, lengthArms, lengthLegs, eyes, hasTail, isFurry):
        self.lengthArms = lengthArms
        self.lengthLegs = lengthLegs
        self.eyes = eyes
        self.hasTail = hasTail
        self.isFurry = isFurry

    def PrintCharacteristics(self):
        print(self.lengthArms)
        print(self.lengthLegs)
        print(self.eyes)
        print(self.hasTail)
        print(self.isFurry)

animal = FavoriteAnimal(1.5, 0.583, 2, True, True)
animal.PrintCharacteristics()
