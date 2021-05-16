from fleet import Fleet
from herd import Herd
from dinosaur import Dinosaur
from robot import Robot
import random


class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def display_welcome(self):
        print('Welcome to the game!')

    # The next few functions generate a game automatically, with randomly selected dinos/robots for each turn (no user control).

    def generate_teams(self):
        self.fleet.create_fleet()
        self.herd.create_herd()

        print(f'\nROBOTS:')
        i = 0
        while i < len(self.fleet.robots):
            print(f'{self.fleet.robots[i].name}')
            i += 1

        print(f'\nDINOSAURS:')
        i = 0
        while i < len(self.herd.dinosaurs):
            print(f'{self.herd.dinosaurs[i].type}')
            i += 1

    def dino_turn(self):
        dino_index = random.randint(0, len(self.herd.dinosaurs) - 1)
        robot_index = random.randint(0, len(self.fleet.robots) - 1)

        current_dino = self.herd.dinosaurs[dino_index]
        current_robot = self.fleet.robots[robot_index]

        print("\n" + Dinosaur.attack(current_dino, current_robot))

        if current_robot.health <= 0:
            print(f'{current_robot.name} health now depleted! {current_robot.name} OUT!')
            self.fleet.robots.remove(current_robot)
        else:
            print(f'{current_robot.name} health now {current_robot.health}')

        if current_dino.energy <= 0:
            print(f'{current_dino.type} energy now depleted! {current_dino.type} OUT!')
            self.herd.dinosaurs.remove(current_dino)

        else:
            print(f'{current_dino.type} energy now {current_dino.energy}')

    def robot_turn(self):
        dino_index = random.randint(0, len(self.herd.dinosaurs) - 1)
        robot_index = random.randint(0, len(self.fleet.robots) - 1)

        current_dino = self.herd.dinosaurs[dino_index]
        current_robot = self.fleet.robots[robot_index]

        print(f'\n{current_robot.name} attacks {current_dino.type} with {current_robot.weapon.type}!')

        Robot.attack(current_robot, current_dino)

        if current_dino.health <= 0:
            print(f'{current_dino.type} health now depleted! {current_dino.type} OUT!')
            self.herd.dinosaurs.remove(current_dino)
        else:
            print(f'{current_dino.type} health now {current_dino.health}')

        if current_robot.power_level <= 0:
            print(f'{current_robot.name} power level now depleted! {current_robot.name} OUT!')
            self.fleet.robots.remove(current_robot)

        else:
            print(f'{current_robot.name} power level now {current_robot.power_level}')

    def run_game(self):
        self.display_welcome()
        self.generate_teams()
        while len(self.herd.dinosaurs) > 0 and len(self.fleet.robots) > 0:
            self.dino_turn()
            if len(self.fleet.robots) > 0:
                self.robot_turn()
        if len(self.herd.dinosaurs) == 0:
            print('Robots win!')
        if len(self.fleet.robots) == 0:
            print('Dinosaurs win!')

    # These functions begin to take user input to control aspects of the game. They'll play as Team Robot.

    def user_fleet_builder(self):
        while True:
            try:
                amount_of_robots = input("How many combatants do you want on each team? Max 5 ")
                amount_of_robots = int(amount_of_robots)
                break
            except ValueError:
                print("\nOops! Enter a number from 1 to 5. ")
        if amount_of_robots > 5 or amount_of_robots <= 0:
            print('\nOops! That number was outside the available range. Your fleet has been set to 5 robots.')
            amount_of_robots = 5
        self.fleet.user_fleet(amount_of_robots)

    def team_setup(self):
        print(f'\nHere is Team Robot: ')
        i = 0
        while i < len(self.fleet.robots):
            name = self.fleet.robots[i].name
            weapon = self.fleet.robots[i].weapon.type
            attack_power = self.fleet.robots[i].weapon.attack_power
            energy_drain = self.fleet.robots[i].weapon.energy_drain
            print(f'{name}: {weapon}, attack power {attack_power}, energy drain per attack {energy_drain}')
            i += 1
        dino_amount = len(self.fleet.robots)
        # while True:
        #     try:
        #         dino_amount = input('\nHow many dinosaurs do you want to fight? ')
        #         dino_amount = int(dino_amount)
        #         break
        #     except ValueError:
        #         print('Oops! Enter the number of dinosaurs you want to fight. ')
        self.herd.create_herd_custom_amount(dino_amount)
        print('\nHere is Team Dinosaur: ')
        i = 0
        while i < len(self.herd.dinosaurs):
            name = self.herd.dinosaurs[i].type
            attack_power = self.herd.dinosaurs[i].attack_power
            energy_drain = self.herd.dinosaurs[i].energy_drain
            print(f'{name}, attack power {attack_power}, energy drain per attack {energy_drain}')
            i += 1

    def show_team_info(self):
        print(f'\nHere is Team Robot: ')
        i = 0
        while i < len(self.fleet.robots):
            name = self.fleet.robots[i].name
            weapon = self.fleet.robots[i].weapon.type
            attack_power = self.fleet.robots[i].weapon.attack_power
            health = self.fleet.robots[i].health
            power_level = self.fleet.robots[i].power_level
            energy_drain = self.fleet.robots[i].weapon.energy_drain
            print(
                f'Robot {i + 1}: {name}, {weapon}, attack power {attack_power}, health {health}, '
                f'power level {power_level}, energy drain per attack {energy_drain}')
            i += 1
        print('\nHere is Team Dinosaur: ')
        i = 0
        while i < len(self.herd.dinosaurs):
            name = self.herd.dinosaurs[i].type
            attack_power = self.herd.dinosaurs[i].attack_power
            health = self.herd.dinosaurs[i].health
            energy = self.herd.dinosaurs[i].energy
            energy_drain = self.herd.dinosaurs[i].energy_drain
            print(f'{name}: attack power {attack_power}, health {health}, energy {energy}, '
                  f'energy drain per attack {energy_drain}')
            i += 1

    def user_robot_turn(self):
        if len(self.fleet.robots) == 1:
            current_robot = self.fleet.robots[0]
        else:
            while True:
                robot_input = input('\nWhich robot do you want to use this turn? ')
                try:
                    robot_index = 6
                    i = 0
                    while i < len(self.fleet.robots):
                        if robot_input == self.fleet.robots[i].name:
                            robot_index = i
                        i += 1
                    current_robot = self.fleet.robots[robot_index]
                    break
                except IndexError:
                    print("Oops! No robots with that name. Try again... ")
        user_select = ''
        while user_select != 'attack' and user_select != 'heal':
            user_select = input(f'\nWould you like to attack a dinosaur, or heal your robot? '
                                f'Healing adds a random number of health points from 5-20 (up to max health), '
                                f'but it costs 15 power level! '
                                f'Enter "attack" or "heal" ')
            if user_select != 'attack' and user_select != 'heal':
                print(f'\nInvalid input! Try again...')
        if user_select == 'heal':
            self.user_robot_heal(current_robot)
        elif user_select == 'attack':
            self.user_robot_attack(current_robot)

    def user_robot_heal(self, robot):
        health_gain = random.randint(5, 20)
        robot.health += health_gain
        if robot.health > 100:
            print(f'{robot.name} health maxed out!')
            robot.health = 100
        else:
            print(f'\n{robot.name} gains {health_gain} health. {robot.name} health now {robot.health}!')
        robot.power_level -= 15
        if robot.power_level > 0:
            print(f'\n{robot.name} power level now {robot.power_level}!')
        elif robot.power_level <= 0:
            print(f'{robot.name} power level now depleted! {robot.name} OUT!')
            self.fleet.robots.remove(robot)

    def user_robot_attack(self, current_robot):
        if len(self.herd.dinosaurs) == 1:
            current_dino = self.herd.dinosaurs[0]
        else:
            current_dino = ''
            while current_dino == '':
                dino_name = 'Dinosaur ' + input('\nWhich dinosaur do you want to attack? Enter their Dinosaur Number: ')
                i = 0
                while i < len(self.herd.dinosaurs):
                    if self.herd.dinosaurs[i].type == dino_name:
                        current_dino = self.herd.dinosaurs[i]
                    i += 1
                if current_dino == '':
                    print(f'\nInvalid input! Try again...')

        print(f'\n{current_robot.name} attacks {current_dino.type} with {current_robot.weapon.type}!')

        Robot.attack(current_robot, current_dino)

        if current_dino.health <= 0:
            print(f'{current_dino.type} health now depleted! {current_dino.type} OUT!')
            self.herd.dinosaurs.remove(current_dino)
        else:
            print(f'{current_dino.type} health now {current_dino.health}')

        if current_robot.power_level <= 0:
            print(f'{current_robot.name} power level now depleted! {current_robot.name} OUT!')
            self.fleet.robots.remove(current_robot)

        else:
            print(f'{current_robot.name} power level now {current_robot.power_level}')

    def run_game_team_robots(self):
        print('You are Team Robot!')
        self.user_fleet_builder()
        self.team_setup()

        user_ready = 'yes'
        while len(self.herd.dinosaurs) > 0 and len(self.fleet.robots) > 0 and user_ready == 'yes':
            self.user_robot_turn()
            user_ready = input('\nReady to continue? Enter "yes" when ready ')
            while user_ready != "yes":
                user_ready = input('\nReady to continue? Enter "yes" when ready ')
            if len(self.herd.dinosaurs) > 0:
                self.dino_turn()
                if len(self.fleet.robots) > 0:
                    user_ready = input('\nReady to continue? Enter "yes" when ready ')
                    while user_ready != "yes":
                        user_ready = input('\nReady to continue? Enter "yes" when ready ')
                    self.show_team_info()

        if len(self.herd.dinosaurs) == 0:
            print('All dinosaurs depleted! Robots win!')
        if len(self.fleet.robots) == 0:
            print('All robots depleted! Dinosaurs win!')
