from battlefield import Battlefield
from robot import Robot
from fleet import Fleet
from dinosaur import Dinosaur


if __name__ == '__main__':
    user_choice = input('Welcome to the game! Do you want to auto-generate a game, '
                        'or do you want to play as Team Robot?'
                        ' (enter "auto"/"robot") ')

    while user_choice == 'auto' or user_choice == 'robot' or user_choice != 'no':
        if user_choice == 'auto':
            Battlefield().run_game()
            user_choice = input('Play again? Enter "auto", "robot", or "no" ')
        elif user_choice == 'robot':
            Battlefield().run_game_team_robots()
            user_choice = input('Play again? Enter "auto", "robot", or "no" ')
        elif user_choice != 'no':
            user_choice = input('Oops! Enter a valid input.')

    if user_choice == 'no':
        print('Thanks for playing!')

    # Dinosaur('dino', 25).attack(Robot('hi'))


