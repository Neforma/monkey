# val = 1
# if val is None:
#     res =[]
# else:
#     res=val
# print(res)
#
# val = None
# res = [] if val is None else val
# print(res)

# dict={x: len(x) for x in ['orange','red','cyan','magenta']}
# print(dict)
#
# sd={(1,2,3): 'Hello'}
# a= sd[(1,2,3)]
# print(a)
# st=(1,2,3)
# print(st,type(st))
# sl=list(st)
# print(sl,type(sl))
# st=([1,2,3],'qwerty')
# st[0].append(4)
# print(st)
# list=[x for x in range(10,100,2) if x % 10 !=0]
# print(list)

#
# import random
#
# class Tank:
#     def __init__(self, model, health, min_damage, max_damage):
#         self.model= model
#         self.health = health
#         self.damage = random.randint(min_damage, max_damage)
#
#     def print_info(self):
#         print(f'{self.model} имеет {self.damage} единиц урона при {self.health} хп')
#
#     def health_down(self, enemy_damage):
#         self.health -= enemy_damage
#         if self.health > 0:
#             print(f'{self.model}:')
#             print(f'Командир, по нашему экипажу попали, у нас осталось {self.health} хп')
#         else:
#             print(f'{self.model}:')
#             print(f'Нас подбили')
#
#     def shot(self,enemy):
#         if enemy.health > 0 and self.health > 0:
#             enemy.health_down(self.damage)
#             print(f'{self.model}:')
#             print(f'Точно в цель, у вражеского танка {enemy.model} осталось {enemy.health} хп')
#         elif enemy.health <=0 and self.health > 0:
#             print(f'Экипаж вражеского танка {enemy.model} уничтожен')
#         else:
#             print(f'{self.model}:')
#             print(f'Выстрел невозможен, нас уже подбили')
#
#
# class SuperTank(Tank):
#
#     def health_down(self, enemy_damage):
#         super().health_down(enemy_damage/2)
#
# supertank1 = SuperTank('ИС-3', 250, 35, 55)
# supertank2 = SuperTank('Maus', 400, 15, 75)
#
# supertank1.print_info()
# supertank2.print_info()
# supertank1.shot(supertank2)
# supertank2.shot(supertank1)


# from tkinter import *
# import random
#
# window = Tk()
# window.title('Game')
#
# w = 600
# h = 600
#
# window.geometry(str(w) + 'x' + str(h))
#
# canvas = Canvas(window, width=w, height=h)
# canvas.place(in_=window, x=0, y=0)
#
# bg_photo = PhotoImage(file='bg_2.png')
#
#
# class Knight:
#     def init(self):
#         self.x = 70
#         self.y = h // 2
#         self.v_y = 0
#         self.v_x = 0
#         self.photo = PhotoImage(file='knight.png')
#
#     def up(self, event):
#         self.v_y = -3
#
#     def down(self, event):
#         self.v_y = 3
#
#     def right(self, event):
#         self.v_x = 3
#
#     def left(self, event):
#         self.v_x = -3
#
#     def stop(self, event):
#         self.v_x = 0
#         self.v_y = 0
#
#
# class Dragon:
#     def init(self):
#         self.x = 750
#         self.y = random.randint(100, 500)
#         self.v = random.randint(2, 4)
#         self.photo = PhotoImage(file='dragon.png')
#
#
# knight = Knight()
# dragons = []
# for i in range(5):
#     dragons.append(Dragon())
#
#
# def game():
#     canvas.delete('all')
#
#     canvas.create_image(300, 300, image=bg_photo)
#     canvas.create_image(knight.x, knight.y, image=knight.photo)
#     knight.y += knight.v_y
#     knight.x += knight.v_x
#     current_dragon = 0
#     dragon_to_kill = -1
#     for dragon in dragons:
#         dragon.x -= dragon.v
#         canvas.create_image(dragon.x, dragon.y, image=dragon.photo)
#
#         if ((dragon.x - knight.x) ** 2 + (dragon.y - knight.y) ** 2) <= 96 ** 2:
#             dragon_to_kill = current_dragon
#
#         current_dragon += 1
#
#         if dragon.x <= 0:
#             canvas.delete('all')
#             canvas.create_text(w // 2, h // 2, font='Verdana 42', fill='red', text='You lose!')
#
#         break
#
#     if dragon_to_kill >= 0:
#         del dragons[dragon_to_kill]
#
#     if len(dragons) == 0:
#         canvas.delete('all')
#         canvas.create_text(w // 2, h // 2, font='Verdana 42', fill='lime', text='You win!')
#
#     else:
#         window.after(5, game)
#
#     def knight_cords():
#         if knight.x + 55 > 600:
#             knight.x = 545
#         if knight.x - 55 < 0:
#             knight.x = 55
#         if knight.y - 60 < 0:
#             knight.y = 60
#         if knight.y + 55 > 600:
#             knight.y = 545
#
#     knight_cords()
#
#
# game()
#
# window.bind('<Key Up>', knight.up)
# window.bind('<Key Down>', knight.down)
# window.bind('<Key Right>', knight.right)
# window.bind('<Key Left>', knight.left)
# window.bind('<KeyRelease>', knight.stop)
#
# window.mainloop()





