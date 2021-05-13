from robot import Robot


class Fleet:
    def __init__(self):
        robot_one = Robot('Optimus Prime')
        robot_two = Robot('Godzilla-bot')
        robot_three = Robot('King Kong-bot')
        self.robots = [robot_one, robot_two, robot_three]
