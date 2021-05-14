class Dinosaur:
    def __init__(self, type, attack_power, energy_drain = -10):
        self.type = type
        self.energy = 100
        self.attack_power = attack_power
        self.health = 100
        self.energy_drain = energy_drain

    def attack(self, robot):
        robot.health -= self.attack_power
        self.energy += self.energy_drain
