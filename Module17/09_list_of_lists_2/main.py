nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

finish_list = [num for list_inside in nice_list for next_list_inside in list_inside for num in next_list_inside]

print(finish_list)