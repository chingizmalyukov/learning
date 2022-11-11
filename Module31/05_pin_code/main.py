import itertools

solution = itertools.combinations_with_replacement('0123456789', 4)
for i_password in solution:
    print(i_password)