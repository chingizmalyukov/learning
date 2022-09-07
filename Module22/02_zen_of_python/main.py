file = open('zen.txt', 'r')
text = []
for i_elem in file:
    text.append(i_elem)
file.close()

for string in reversed(text):
    print(string, end='')
