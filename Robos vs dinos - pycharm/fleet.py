from robot import Robot


class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self):
        self.robots.append(Robot('Optimus Prime'))
        self.robots.append(Robot('Godzilla-bot'))
        self.robots.append(Robot('King Kong-bot'))

    def user_fleet(self, amount):
        self.robots = []
        i = 1
        while i <= amount:
            robot_name = input(f'Robot {i} - enter name: ')
            self.robots.append(Robot(robot_name))
            self.robots[i-1].choose_weapon()
            i += 1


