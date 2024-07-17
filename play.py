from error_process import max_row, max_column, restore_times, win_condition
from player import player1
import random

choice_value = (2, 4, 8, 16, 32)
weight = (0.6, 0.25, 0.1, 0.04, 0.01)

class CircularIteratorIndex:
    def __init__(self) -> None:
        self.index = 0

    def __next__(self):
        self.index = (self.index + 1) % restore_times
        return self.index

    def __previous__(self):
        self.index = (self.index - 1) % restore_times
        return self.index

    def __current__(self):
        return self.index

index_iterator = CircularIteratorIndex()
# index_iterator.__next__()
# print(index_iterator.index)


class Numbers:
    def __init__(self) -> None:

        self._data_dict = {}
        self._score_dict = {}
        for i in range(restore_times):
            self._data_dict[i] = []
            self._score_dict [i] = 0

        for x in range(max_row):
            row = []
            for y in range(max_column):
                row.append(None)
            self._data_dict[0].append(row)

    def random_generator(self):
        split = False

        def none_checker(data):
            index = []
            for index_row, item in enumerate (data):
                for index_column, item2 in enumerate(item):
                    if item2 == None:
                        index.append([index_row,index_column])
            return index
        
        def random_indenx_with_split(rand_number,check_idenx):
            if rand_number == 2:
                if random.choices((1,2),weights=(0.6,0.4),k=1)[0] == 2:
                    nonlocal split
                    rand_index_list = random.choices(check_idenx,k=2)
                    split = True
                    return rand_index_list
                else :
                    rand_index = random.choice(check_index)
                    return rand_index
            else:
                rand_index = random.choice(check_index)
                return rand_index
                        
        current_index = index_iterator.__current__()
        check_index = none_checker(self._data_dict[current_index])
        if check_index:
            rand_number = random.choices(choice_value, weights=weight, k=1)[0]
            rand_index = random_indenx_with_split(rand_number, check_index)
            # print (split)
            if split == True:
                rand_index1,rand_index2 = rand_index
                self._data_dict[current_index][rand_index1[0]][rand_index1[1]] = rand_number
                self._data_dict[current_index][rand_index2[0]][rand_index2[1]] = rand_number
            else:
                self._data_dict[current_index][rand_index[0]][rand_index[1]] = rand_number
        else:
            player1.win = False

    def moving(self, temp_row):
        temp_index = 0
        temp_number = None
        for index, item2 in enumerate(temp_row):
            if item2 != None:
                temp_row[temp_index] = item2
                if temp_index != index:
                    temp_row[index] = None
                if temp_number == item2:
                    item3 = item2 * 2
                    temp_index -= 1
                    temp_row[temp_index] = item3
                    temp_row[temp_index + 1] = None
                    player1.score += item3
                    if item3 == win_condition:
                        player1.win = True
                temp_number = item2
                temp_index += 1
        return temp_row
    
    def score(self, index):
        self._score_dict[index] = player1.score

    def moving_left(self):
        current_index = index_iterator.__current__()
        temp_row_list = list(map(self.moving, self._data_dict[current_index]))
        current_index_a = index_iterator.__next__()
        self._data_dict[current_index_a] = temp_row_list
        self.score(current_index_a)

    def moving_right(self):
        current_index = index_iterator.__current__()
        temp_row_list = list(
            map(
                lambda row_for_temp: self.moving(row_for_temp[::-1])[::-1],
                self._data_dict[current_index],
            )
        )
        current_index_a = index_iterator.__next__()
        self._data_dict[current_index_a] = temp_row_list
        self.score(current_index_a)

    def moving_up(self):
        current_index = index_iterator.__current__()
        matrix = [
            [row[i] for row in self._data_dict[current_index]]
            for i in range(len(self._data_dict[current_index][0]))
        ]
        temp_row_list = list(map(self.moving, matrix))
        matrix = [
            [row[i] for row in temp_row_list] for i in range(len(temp_row_list[0]))
        ]
        current_index_a = index_iterator.__next__()
        self._data_dict[current_index_a] = matrix
        self.score(current_index_a)

    def moving_down(self):
        current_index = index_iterator.__current__()
        matrix = list(zip(*self._data_dict[current_index]))
        matrix = [list(item)[::-1] for item in matrix]
        temp_row_list = list(map(self.moving, matrix))
        matrix = [item[::-1] for item in temp_row_list]
        matrix = list(zip(*matrix))
        matrix = [list(item) for item in matrix]
        current_index_a = index_iterator.__next__()
        self._data_dict[current_index_a] = matrix
        self.score(current_index_a)
    
    def reverse(self):
        current_index = index_iterator.__previous__()
        player1.score = self._score_dict[current_index]
    
    def get_current_data(self):
        current_index = index_iterator.__current__()
        current_data = self._data_dict[current_index]
        return current_data
    
    def get_current_score(self):
        current_index = index_iterator.__current__()
        current_score = self._score_dict[current_index]
        return current_score
    
playing = Numbers()
# generater_read = Numbers()

# a = Numbers()
# a.random_generator()
# # a.moving_left()
# # a.moving_right()
# # a.moving_up()
# # a.moving_down()
# print(a._data_dict)
# c = a.get_current_data()
# print(c)
