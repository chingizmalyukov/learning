numbers_count = 3
lists_count = 4

finish_list = [list(range(x, x + lists_count * (numbers_count - 1) + 1, lists_count))
               for x in range(1, lists_count + 1)]

print(finish_list)
