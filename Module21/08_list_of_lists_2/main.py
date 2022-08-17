def flat(nice_list, new_list):
    for item in nice_list:
        if isinstance(item, list):
            flat(item, new_list)
        else:
            new_list.append(item)
    return new_list


new_list = []
nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

print(flat(nice_list, new_list))
