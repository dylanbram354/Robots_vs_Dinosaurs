from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.power_level = 100
        self.health = 100
        self.weapon = Weapon('big scary laser gun', 20)

    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        self.power_level -= 10
