'''class Point:
    def __init__(self, a=0, b=0, c=0):
        self.a= a
        self._b= b
        self.__c= c

    def set_point(self,a,b,c):
        self.__c = c

    def get_point(self):
        return self.a, self._b, self.__c


pt= Point(1,2,3)
pt.a=5
pt._b=6
pt.set_point(1,2,7)

print(pt.get_point())  '''


'''class Point:
    def __new__(cls, *args, **kwargs):
        print('New: ',str(cls))
        return super().__new__(cls)

    def __init__(self, a=0,b=0):
        print('Init:',str(self))
        self.a = a
        self.b = b


pt = Point(1,2)
print(pt)'''

#
# class Singleton(object):
#     def __new__(cls):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super(Singleton, cls).__new__(cls)
#         return cls.instance
#
#
# s = Singleton()
# print('Создание объекта:', s, id(s))
# s1 = Singleton()
# print('Создание объекта 1 :', s1, id(s1))


'''def repair_deco(func):
    def wrapper(a, b):
        return func(a, b) - 1
    return wrapper


@repair_deco
def wrong_func(a, b):
    return a + b + 1


print(f'2+2={wrong_func(2,2)}')'''

# from datetime import datetime
#
#
# def timeit(func):
#     def wrapper(val):
#         start = datetime.now()
#         res = func(val)
#         end = datetime.now()
#         print(f'time: {end-start}')
#         return res
#     return wrapper
#
#
# @timeit
# def get_list_1(val):
#     return [x for x in range(val) if x % 2]
#
#
# @timeit
# def get_list_2(val):
#     nl=[]
#     for x in range(val):
#         if x % 2:
#             nl.append(x)
#     return nl
#
# val = 1000000000
#
# a=get_list_1(val)
# b=get_list_2(val)
# age = 18
#
# is_allow = True if age >= 18 else False
#
# print(is_allow)