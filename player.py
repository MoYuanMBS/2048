from error_process import username
from enum import Enum

class Player():
    def __init__(self) -> None:
        self.name = username
        self.score = 0
        self.win:Player.State = Player.State.Nonee
        self.playtimes = 0
    class State(Enum):
        Win = 1
        Loose = -1
        Nonee = 0
    
player1 = Player()