from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.power_level = 100
        self.health = 100
        self.weapon = Weapon('laser gun', 20)

    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        self.power_level += self.weapon.energy_drain

    def choose_weapon(self):
        option_1 = Weapon('laser gun', 20, -10)
        option_2 = Weapon('rocket launcher', 30, -20)
        option_3 = Weapon('sword', 25, -15)
        options = [option_1, option_2, option_3]
        print(f"Choose this robot's weapon:")
        i = 1
        while i <= len(options):
            print(f"Option {i}: {options[i-1].type}, attack power {options[i-1].attack_power}, energy drain {options[i-1].energy_drain}")
            i += 1
        user_choice = input('Enter your choice. For Option 1, enter 1. Etc... ')
        user_choice = int(user_choice)-1
        chosen_weapon = options[user_choice]
        self.weapon = chosen_weapon


