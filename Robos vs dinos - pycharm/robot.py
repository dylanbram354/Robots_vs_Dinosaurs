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
        print(f"\nChoose this robot's weapon:\n")
        i = 1
        while i <= len(options):
            print(f"Option {i}: {options[i-1].type}, attack power {options[i-1].attack_power}, energy drain per attack {options[i-1].energy_drain}")
            i += 1
        while True:
            try:
                user_choice = input('\nEnter your choice. For Option 1, enter 1. Etc... ')
                user_choice = int(user_choice) - 1
                if user_choice >= len(options) or user_choice < 0:
                    user_choice = len(options) - 1
                    print(f"Oops! That number wasn't an option. Option {user_choice + 1} selected by default.")
                break
            except ValueError:
                print("Oops! Enter a number corresponding with the weapon you want to assign.")
        chosen_weapon = options[user_choice]
        self.weapon = chosen_weapon


