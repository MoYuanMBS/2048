    # def moving_down(self):
    #     current_index = index_iterator.__current__()
    #     matrix = [
    #         [row[i] for row in self._data_dict[current_index]][::-1]
    #         for i in range(len(self._data_dict[current_index][0]))
    #     ]
    #     temp_row_list = list(map(self.moving, matrix))
    #     matrix = [
    #         [row[i] for row in temp_row_list][::-1]
    #         for i in range(len(temp_row_list[0]))
    #     ]
    #     current_index_a = index_iterator.__next__()
    #     self._data_dict[current_index_a] = matrix

import random 

data = [
    [1,2,3],
    [2,5,6],
    [7,8,9],
    [0,4,3]

]
b=[]
print(data)
a = list(zip(*data))
print (a)
a = [list(item)[::-1] for item in a]
print (a)
a = [item[::-1] for item in a]
print (a)
a = list(zip(*a))
print(a)
a = [list(item) for item in a]
print(a)

class SB():
    def __init__(self) -> None:
        self.asd = 0

sb = SB()
print(sb.asd)
sb.asd = True
print(sb.asd)

data2 = [
    [1,2],
    [3,4]
]

if random.choices((1,2), weights=(0.7,0.3), k=1)[0] == 2 :
    try:
        a = random.choices(data2,k=3)
    except IndexError:
        a = None
else:
    a = 3
print (a)
a,b = data2
print (a)
print (b)

a,b = data2

if data2:
    print ('yes')

c = False

def ree ():
    global c
    c = True
    return c

d = ree()

print (c)
print (d)

e = random.choice(data2)
print (e)

class A ():
    def __init__(self) -> None:
        pass

    def aa(self):
        f = True
        def bb():
            # nonlocal f
            f = False
            return f
        g = bb()
        return f,g
d = A()
f,g = d.aa()
print (f'{f}\n{g}')