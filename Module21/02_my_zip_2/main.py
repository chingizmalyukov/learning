def my_zip(*args):
    length = min(len(element) for element in args)
    tpl_list = [tuple(struct[i] for struct in map(list, args)) for i in range(length)]

    return tpl_list

a = [{"x": 4}, "b", "z", "d"]
b = (10, {20,}, [30], "z")
print(my_zip(a, b))