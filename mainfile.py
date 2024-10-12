from player import player1,Player
from play import playing
from generater import generater
from error_process import user_input

user_input.checked_valu_return()

def user_state (func) -> None:
        move_available = func()
        if move_available is True:
            playing.random_generator()
            playing.win_lose_moving_checking()
            print (player1.win)
            if player1.win is Player.State.Win:
                generater.print_full_grid()
                generater.print_win()
                return
            if player1.win is Player.State.Loose:
                generater.print_full_grid()
                generater.print_loose()
                return
            generater.print_full_grid()
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
    else:
        if result == 'R':
            playing.reverse()
            generater.print_full_grid()

def one_time_playing ():
    playing.random_generator()
    generater.print_full_grid()
    while player1.win is Player.State.Nonee:
        user_playing()
    player1.playtimes += 1

if player1.playtimes == 0:
    one_time_playing()
else:
    restart_input = user_input.user_input()
    if user_input == 'R':
        temp_playtimes = player1.playtimes
        playing.reset_games()
        one_time_playing()
        player1.playtimes = temp_playtimes + 1

# playing.random_generator()
# c = playing.get_current_data()
# generater.print_full_grid() 
# print(c)    
# user_playing(playing.moving_left)