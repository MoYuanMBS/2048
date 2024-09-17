from player import player1
from play import playing
from generater import generater
from error_process import user_input

# while player1.win is False:
#     playing.random_generator()

user_input.checked_valu_return()

def user_state (func):
        func()
        if player1.win is True:
            generater.print_full_grid
            generater.print_win()
            return
        elif player1.win is False:
            generater.print_full_grid
            generater.print_loose()
            return
        else:
            pass
            return
def user_playing ():
    result = user_input.user_input()
    imput_set = {'A','W','S','D'}
    if result in imput_set:
        if result == 'A':
            user_state(playing.moving_left)
        elif result == 'D':
            user_state(playing.moving_right)
        elif result == 'W':
            user_state(playing.moving_up)
        elif result == 'S':
            user_state(playing.moving_down)
        playing.random_generator()
        generater.print_full_grid()
    else:
        if result == 'R':
            playing.reverse()
            generater.print_full_grid()

def one_time_playing ():
    playing.random_generator()
    generater.print_full_grid()
    while player1.win == 0:
        user_playing()
    player1.playtimes += 1

if player1.playtimes == 0:
    one_time_playing()
else:
    restart_input = user_input.user_input()
    if user_input == 'R':
        one_time_playing()
# playing.random_generator()
# c = playing.get_current_data()
# generater.print_full_grid() 
# print(c)    
# user_playing(playing.moving_left)