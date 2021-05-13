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
        dino_index = random.randint(0, len(self.herd.dinosaurs)-1)
        robot_index = random.randint(0, len(self.fleet.robots)-1)

        current_dino = self.herd.dinosaurs[dino_index]
        current_robot = self.fleet.robots[robot_index]

        print(f'\n{current_dino.type} attacks {current_robot.name}!')

        Dinosaur.attack(current_dino, current_robot)

        if current_robot.health <= 0:
            print(f'{current_robot.name} health now depleted! {current_robot.name} OUT!')
            self.fleet.robots.remove(current_robot)
        else:
            print(f'{current_robot.name} health now {current_robot.health}')

        if current_dino.energy <= 0:
            print(f'{current_dino.name} energy now depleted! {current_dino.name} OUT!')
            self.herd.dinosaurs.remove(current_robot)

        else:
            print(f'{current_dino.type} energy now {current_dino.energy}')

    def robot_turn(self):
        dino_index = random.randint(0, len(self.herd.dinosaurs)-1)
        robot_index = random.randint(0, len(self.fleet.robots)-1)

        current_dino = self.herd.dinosaurs[dino_index]
        current_robot = self.fleet.robots[robot_index]

        print(f'\n{current_robot.name} attacks {current_dino.type}!')

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
        amount_of_robots = input("How many bots do you want on your team? Max 5 ")
        amount_of_robots = int(amount_of_robots)
        if amount_of_robots > 5:
            amount_of_robots = 5
        self.fleet.user_fleet(amount_of_robots)

    def user_robot_turn(self):
        pass

    def show_info_team_robot(self):
        print(f'\nHere is your fleet: ')
        i = 0
        while i < len(self.fleet.robots):
            name = self.fleet.robots[i].name
            weapon = self.fleet.robots[i].weapon.type
            attack_power = self.fleet.robots[i].weapon.attack_power
            print(f'{name}, {weapon}, attack power {attack_power}')
            i += 1
        dino_amount = input('How many dinosaurs do you want to fight?')
        dino_amount = int(dino_amount)
        self.herd.create_herd_custom_amount(dino_amount)
        print('\nHere is Team Dinosaur: ')
        i = 0
        while i < len(self.herd.dinosaurs):
            name = self.herd.dinosaurs[i].type
            attack_power = self.herd.dinosaurs[i].attack_power
            print(f'{name}, attack power {attack_power}')
            i += 1

    def run_game_team_robots(self):
        self.display_welcome()
        print('You are Team Robot!')
        self.user_fleet_builder()
        self.show_info_team_robot()











