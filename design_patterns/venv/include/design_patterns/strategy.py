class FlyWithRocket:
    def __init__(self):
        pass

    def fly(self):
        print("Flying with rocket")


class FlyWithWings:
    def __init__(self):
        pass

    def fly(self):
        print("Flying with wings")


class CantFly:
    def __init__(self):
        pass

    def fly(self):
        print("I cant fly")


class SuperDuck:
    def __init__(self):
        pass

    def set_flying_behaviour(self, fly_obj):
        self.fly_obj = fly_obj

    def perfom_fly(self):
        self.fly_obj.fly()


if __name__ == '__main__':
    duck = SuperDuck()
    fly_behaviour = FlyWithRocket()
    duck.set_flying_behaviour(fly_behaviour)
    duck.perfom_fly()