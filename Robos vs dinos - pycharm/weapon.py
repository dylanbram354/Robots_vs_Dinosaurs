class Weapon:
    def __init__(self, type, attack_power, energy_drain=-10):
        self.type = type
        self.attack_power = attack_power
        self.energy_drain = energy_drain