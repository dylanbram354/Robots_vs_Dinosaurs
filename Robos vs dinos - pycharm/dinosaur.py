class Dinosaur:
    def __init__(self, type, attack_power):
        self.type = type
        self.energy = 100
        self.attack_power = attack_power
        self.health = 100

    def attack(self, robot):
        robot.health -= self.attack_power
        self.energy -= 10
