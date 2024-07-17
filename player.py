from error_process import username

class Player():
    def __init__(self) -> None:
        self.name = username
        self.score = 0
        self.win = 0
player1 = Player()
# review suggestion:
# 不要使用player1这样没有意义的名字喂，除非是要做多人对战联机或者同时操作一个WASD一个↑↓←→，不然建议换个变量名如player_default之类
