def is_prime(n):  # NOTE нейминг!
    if n == 1:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


string = 'О Дивный Новый мир!'
solution = [symbol for index, symbol in enumerate(string) if is_prime(index)]
print(solution)
