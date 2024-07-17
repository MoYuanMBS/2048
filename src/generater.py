from enum import Enum

from rich.console import Console
from rich.text import Text

from error_process import loose_text, max_row, win_text
from play import playing
from player import player1

console = Console(force_terminal=True, color_system="truecolor")


def print_colored_text(text, color):
    styled_text = Text(text, style=f"color({color})")
    console.print(styled_text)


# print (player1.name)


class BasicGrid(object):
    def __init__(self) -> None:
        self.grid_row = "--------"
        self.grid_top_bottom = "|       "


class Generater(BasicGrid):
    def center_text(self, text, length=7):
        text = str(text)
        front = (length - len(text)) // 2
        back = length - len(text) - front
        return " " * front + text + " " * back

    def grid_generater_top(self):
        console.print(self.grid_row * max_row + "-")
        console.print(self.grid_top_bottom * max_row + "|")

    def grid_generater_end(self):
        console.print(self.grid_row * max_row + "-")

    def grid_generater_bottom(self):
        console.print(self.grid_top_bottom * max_row + "|")

    def grid_generater_middle(self, row_content: list):
        text_middle = []
        for num in row_content:
            if num is not None:
                num_color_code = ColorList.colorlize(num)
                num = self.center_text(num)
                num = Text(str(num), style=f"bold {num_color_code}")
                text_middle.append(num)
            else:
                text_middle.append(Text(" " * 7))
        combined_text = Text("|") + Text("|").join(text_middle) + Text("|")
        console.print(combined_text)

    @staticmethod
    def information_decorator(function):
        def inner(*agars, **kwagars):
            print(player1.name)
            print(f"Score={playing.get_current_score()}")
            function(*agars, **kwagars)

        return inner

    @information_decorator
    def print_full_grid(self):
        content = playing.get_current_data()
        for row_content in content:
            self.grid_generater_top()
            self.grid_generater_middle(row_content)
            self.grid_generater_bottom()
        self.grid_generater_end()

    def win_loose_text(self, text):
        text = player1.name + text
        color_code = ColorList.colorlize(text)
        centered_text = self.center_text(text, length=max_row)
        console.print(Text(str(centered_text), style=f"bold {color_code}"))

    @information_decorator
    def print_win(self):
        self.win_loose_text(win_text)

    @information_decorator
    def print_loose(self):
        self.win_loose_text(loose_text)


class ColorList(Enum):
    color_2 = "#F3E3BB"
    color_4 = "#F1D591"
    color_8 = "#E7BC54"
    color_16 = "#F1AF67"
    color_32 = "#E58214"
    color_64 = "#F19667"
    color_128 = "#EE7333"
    color_256 = "#F16F69"
    color_512 = "#E7362E"
    color_1024 = "#F1DC2E"
    color_2048 = "#BF0000"
    color_other = "#BF0000"

    @staticmethod
    def colorlize(text: str | int):
        text = "color_" + str(text)
        if hasattr(ColorList, text):
            return getattr(ColorList, text).value
        else:
            return ColorList.color_other.value


generater = Generater()
# generater_read.random_generator()
# generater_read.random_generator()
# generater_read.random_generator()
# generater_read.random_generator()
# generater_read.random_generator()
# generater_read.random_generator()
# generater.print_full_grid()
# generater.print_win()
# generater.print_loose()


"""
---------
|       |
|  128  |    
|       |
-----------
|       |
|       |   
|       |     
"""
