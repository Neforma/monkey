

# a = [x for x in range(1, 100_000)]

# a = (x for x in range(1, 100_000))
# print(a)
# for i in a:
#     print(i)

# def gen():
#     for x in range(100):
#         print(f'Do {x}')
#         yield x
#         print(f'Posle {x}')
#
# print(gen())
#
# for i in gen():
#     print(i)

# file = open('file.txt', 'w')
# file.write(['hello', 20021, 29391])
# file.close()
# list=[]
# for i in range(1000):
#     file = open('file.txt', 'w')
#     list.append(file)
#     file.close


with open('file.txt', 'w') as f:
    f.write('hello')