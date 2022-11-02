import math

solution = []

for i in range(2, 1001):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        solution.append(i)
print(solution)


print(list(filter(lambda n: (math.factorial(n - 1) + 1) % n == 0,
                  range(2, 1000))))  # теорема Вильсона смотрится проще, но с большими числами работает долго

print(print(list(filter(lambda x: all(map(lambda i: x % i != 0, range(2, int(x ** 0.5) + 1))),
                        range(2, int(input()) + 1)))))  # естественно не сам я это писал

# ответ на вопрос: "да"
