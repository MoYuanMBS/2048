from error_process import user_input
from generater import generater
from play import playing
from player import player1

# while player1.win is False:
#     playing.random_generator()

user_input.checked_valu_return()


def user_playing(func):
    func()
    playing.random_generator()
    generater.print_full_grid()
    if player1.win is True:
        generater.print_win()
    elif player1.win is False:
        generater.print_loose()
    else:
        pass


playing.random_generator()
generater.print_full_grid()
while player1.win == 0:
    result = user_input.user_input()
    if result == "A":
        user_playing(playing.moving_left)
    elif result == "D":
        user_playing(playing.moving_right)
    elif result == "W":
        user_playing(playing.moving_up)
    elif result == "S":
        user_playing(playing.moving_down)
    elif result == "R":
        playing.reverse()
        generater.print_full_grid()

# playing.random_generator()
# c = playing.get_current_data()
# generater.print_full_grid()
# print(c)
# user_playing(playing.moving_left)
