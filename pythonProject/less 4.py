# class Item:
#     def __init__(self, name, price, weight):
#         self.name = name
#         self.price = price
#         self.weight = weight
#
#     def __add__(self, other):
#         if isinstance(other, Item):
#             return self.price + other.price
#         elif isinstance(other, int):
#             return self.price + other
#         # tot_pr = self.price + other.price
#         # return tot_pr
#
#
# it1 = Item('Видюха', 15000, 0)
# it2 = Item('Проц', 12000, 0)
# print(it1 + 10000)

from tkinter import *
from random import randint

win = Tk()
win.geometry('600x600')


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


canvas = Canvas(win, width=600, height=600)
canvas.pack()

elements = [Fire(), Earth(), Wind(), Water()]

for elem in elements:
    img = canvas.create_image(randint(50, 550), randint(50,550), image=elem.image)


def move(event):
    img_id = canvas.find_overlapping(event.x, event.y, event.x+10, event.y+10)
    if len(img_id) == 2:
        element_1 = elements[img_id[0] - 1]
        element_2 = elements[img_id[1] - 1]
        new_element = element_1 + element_2
        print(new_element)
        if new_element:
            if new_element not in elements:
                canvas.create_image(event.x, event.y, image=new_element.image)
                elements.append(new_element)

    canvas.coords(img_id, event.x, event.y)


win.bind('<B1-Motion>', move)
win.mainloop()