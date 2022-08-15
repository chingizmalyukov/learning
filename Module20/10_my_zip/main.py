def action(Left, Right):
    for i in range(min(len(Left), len(Right))):
        yield Left[i], Right[i]

string = 'abcd'
numbers = (10, 20, 30, 40, 50)
solution = action(string, numbers)
print('\nРезультат:\n', solution)
for letter, dig in solution:
    print((letter, dig))
