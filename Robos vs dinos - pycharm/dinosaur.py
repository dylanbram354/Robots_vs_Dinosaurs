import random


class Dinosaur:
    def __init__(self, type, attack_power, energy_drain = -10):
        self.type = type
        self.energy = 100
        self.attack_power = attack_power
        self.health = 100
        self.energy_drain = energy_drain

    def attack(self, robot):
        attack_types = ('claw', 'bite', 'tail', 'kick', 'special')
        attack = random.choice(attack_types)
        attack_statement = f'{self.type} uses {attack} attack against {robot.name}!'
        if attack == 'special':
            attack_statement += f'\nIt does extra damage! But, it drains more energy...'
            robot.health -= self.attack_power + 10
            self.energy += self.energy_drain - 10
        else:
            robot.health -= self.attack_power
            self.energy += self.energy_drain
        return attack_statement
