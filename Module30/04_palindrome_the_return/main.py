from collections import Counter


def can_be_poly(text):
    solution = list(filter(lambda x: x % 2 != 0, Counter(text).values()))
    if len(solution) <= 1:
        return True
    return False


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))

# после объяснения работы Counter, сделал задачу минут за 10, играя в телефон параллельно
