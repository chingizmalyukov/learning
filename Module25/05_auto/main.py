list = [10, 20, 30]

iterator = list.__iter__()
try:
    while True:
        print(next(iterator))
except StopIteration:
    print('Цикл закончился')