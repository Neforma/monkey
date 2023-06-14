# # import time
# #
# #
# # class RunningCodeJudge:
# #     def __init__(self):
# #         self.start= None
# #
# #     def __enter__(self):
# #         self.start = time.time()
# #
# #     def __exit__(self, exc_type, exc_val, exc_tb):
# #         t = time.time() - self.start
# #         print(f'Время работы кода: {t} сек')
# #
# #
# # with RunningCodeJudge():
# #     mlist = [x for x in range(1, 100_000)]
#
# # ml = [1,2,3,4,5]
# # # for i in ml:
# # #     print(i)
# # list_it = iter(ml)
# # print(next(list_it))
# import random
#
#
# class RandIter:
#     def __init__(self, limit):
#         self.limit = limit
#         self.__reload = limit
#
#     def __iter__(self):
#         self.limit = self.__reload
#         return self
#     def __next__(self):
#         if self.limit == 0:
#             raise StopIteration
#
#         self.limit -= 1
#         return random.randint(1, 100)
#
#
# rand_iter = RandIter(5)
# print(next(rand_iter))
# print(next(rand_iter))
# print(next(rand_iter))
#
# rand_iter = iter(rand_iter)
# print(next(rand_iter))
# print(next(rand_iter))
# print(next(rand_iter))
# print(next(rand_iter))
# print(next(rand_iter))
#
from tkinter import *
from random import randint

window = Tk()
window.geometry('600x600')


class Fire:
    image = PhotoImage(file='elements/free-icon-fire-9509865.png').subsample(4, 4)
    def __add__(self, other):
        if isinstance(other, Earth):
            return Clay

class Wind:
    image = PhotoImage(file='elements/wind.png').subsample(4, 4)

class Earth:
    image = PhotoImage(file='elements/ground.png').subsample(4, 4)
    def __add__(self, other):
        if isinstance(other, Fire):
            return Clay

class Water:
    image = PhotoImage(file='elements/free-icon-water-drop-4246703.png').subsample(4, 4)

class Clay:
    image = PhotoImage(file='elements/free-icon-pottery-7942410.png').subsample(4, 4)


canvas = Canvas(window, width=600, height=600)
canvas.pack()

elements = [Fire(), Earth(), Wind(), Water()]

for elem in elements:
    img = canvas.create_image(randint(50, 550), randint(50, 550), image=elem.image)


def move(event):
    images_id = canvas.find_overlapping(event.x, event.y, event.x+10, event.y+10)
    if len(images_id) == 2:
        element_1 = elements[images_id[0] - 1]
        element_2 = elements[images_id[1] - 1]
        new_element = element_1 + element_2
        print(new_element)
        if new_element:
            if new_element not in elements:
                canvas.create_image(event.x, event.y, image=new_element.image)
                elements.append(new_element)

    canvas.coords(images_id, event.x, event.y)

    print(images_id)



window.bind('<B1-Motion>', move)

window.mainloop()
