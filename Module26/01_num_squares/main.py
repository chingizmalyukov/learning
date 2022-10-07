class Iterator:
    step = 0

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.step < self.n:
            self.step += 1
            return self.step ** 2
        else:
            # raise Exception('Числа закончились!')  # как остановить итератор по-другому, не через ошибку?
            raise StopIteration  # NOTE используйте другой класс исключения


def generator(n):
    for num in range(1, n + 1):
        yield num ** 2


n = 3

print(list(generator(n)))

solution = list((x ** 2 for x in range(1, n + 1)))
print(solution)

iter = Iterator(3)
for i_num in iter:
    print(i_num, end=' ')
