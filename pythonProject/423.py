# def rec(count):
#     print(count)
#     if count == 5:
#         return
#     rec(count + 1)
#     print(count)
#
#
# rec(0)
import os

current_path = os.path.abspath(__file__)
parr_path = os.path.join(current_path, '..')


def get_all_path(path):
    for name in os.listdir(path):
        new_path = os.path.join(path, name)
        if os.path.isdir(new_path):
            print('Папка', name)
            get_all_path(new_path)
        else:
            print(' -', name)


get_all_path(parr_path)

