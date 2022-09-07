
file = open('text.txt')
solution = open('cipher_text.txt', 'a')

for i, i_elem in enumerate(file):
    string = ''
    for j_elem in i_elem:
        if j_elem == '\n':
            break
        code = ord('a') + (ord(j_elem) - ord('a') + (i + 1) % (ord('z') - ord('a') + 1))
        string += chr(code)
    solution.write(string)
    solution.write('\n')

file.close()
solution.close()
