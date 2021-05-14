from battlefield import Battlefield
from robot import Robot
from fleet import Fleet



if __name__ == '__main__':
    user_choice = input('Welcome to the game! Do you want to auto-generate a game, '
                        'or do you want to play as Team Robot?'
                        ' (enter "auto"/"robot") ')
    while user_choice != 'no':
        if user_choice == 'auto':
            Battlefield().run_game()
        else:
            Battlefield().run_game_team_robots()
        user_choice = input('Play again? Enter "auto", "robot", or "no" ')


