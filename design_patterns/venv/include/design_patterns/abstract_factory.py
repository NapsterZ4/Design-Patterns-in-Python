import random


class PetShop(object):
    def __init__(self, animal_factory=None):
        self.pet_factory = animal_factory

    def show_pet(self):
        pet = self.pet_factory()
        print("We have a {}".format(pet))
        print("It says: {}".format(pet.speak()))


class Dog:
    def speak(self):
        return "Woof"

    def __str__(self):
        return "Dog"


class Cat:
    def speak(self):
        return "Miau"

    def __str__(self):
        return "Cat"


def random_animal():
    return random.choice([Dog, Cat])()


if __name__ == '__main__':
    shop = PetShop(random_animal)
    for i in range(4):
        shop.show_pet()
        print("=" * 25)