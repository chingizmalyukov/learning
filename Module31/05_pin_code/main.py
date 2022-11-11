import itertools

digits = range(10)
pincode_vars = itertools.product(digits, repeat=4)
print(len(list(pincode_vars)))
