from settings import username, max_column, max_row, restore_times, win_condition

win_text = '一定是侥幸赢了呢！哼！'
loose_text = '肯定会输的啦~'

class TrySettings():
    
    # def __init__(self) -> None:
    #     pass
    @ staticmethod
    def username_check():
        checked_username = '米小子是你了'
        try:
            checked_username = str(username)
        except TypeError:
            print('您只有一个名字哦！')
        except ValueError:
            print('你小子编辑一个正常的东西作为名字！')
        except MemoryError:
            print('你在搞事情？！')
        return checked_username

    @ staticmethod
    def max_column_check():
        checked_max_column = 5
        try:
            checked_max_column = abs(int(max_column))
            if checked_max_column == 0:
                checked_max_column += 1
        except TypeError:
            print('max_column只能有一个数啊喂！')
        except ValueError:
            print('请给max_column输入正常的数字')
        return checked_max_column

    @ staticmethod
    def max_row_check():
        checked_max_row = 5
        try:
            checked_max_row = abs(int(max_row))
            if checked_max_row == 0:
                checked_max_row += 1
        except TypeError:
            print('max_row只能有一个数啊喂！')
        except ValueError:
            print('请给max_row输入正常的数字')
        return checked_max_row

    @ staticmethod    
    def restore_times_check():
        checked_restore_times = 2
        try:
            checked_restore_times = abs(int(restore_times)) +1
        except TypeError:
            print('restore_times只能有一个数啊喂！')
        except ValueError:
            print('请给restore_times输入正常的数字')
        return checked_restore_times

    @ staticmethod
    def win_condition_check():
        checked_win_condition = 2048
        def number_generater():
            num_list = set()
            i = 2
            while i <= 9999999:
                i *= 2
                num_list.add(i)
            return num_list
        try:
            checked_win_condition = abs(int(win_condition))
            if checked_win_condition in number_generater() and checked_win_condition>=64:
                return checked_win_condition
            else:
                print('填一个>64的2的平方数啊亲！')
        except TypeError:
            print('wincondition只能有一个数啊喂！')
        except ValueError:
            print('请给wincondition输入正常的数字')
        return win_condition

class UserImput():
    
    def checked_valu_return(self):
        global username, max_column, max_row, restore_times, win_condition
        username = TrySettings.username_check()
        max_column = TrySettings.max_column_check()
        max_row = TrySettings.max_row_check()
        restore_times = TrySettings.restore_times_check()
        win_condition = TrySettings.win_condition_check()
    
    def user_input(self):
        print('请输入操作步骤：')
        correct = False
        while correct is False:
            try:
                input_content = input()
                input_content = input_content.upper().strip()
                if input_content in (inputs := ('A','W','S','D','R')):
                    correct = True
                    return input_content
                else:
                   print('请输入正确操作') 
            
            except TypeError:
                print('请输入正确操作')
            except ValueError:
                print('请输入正确操作')

user_input = UserImput()

