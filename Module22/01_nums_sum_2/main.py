solution = 0

file = open('numbers.txt', 'r')
for i_elem in file:
    for j_elem in i_elem:
        if j_elem.isdigit():
            solution += int(j_elem)
file.close()

answer = open('answer.txt', 'w')
answer.write(str(solution))
answer.close()
