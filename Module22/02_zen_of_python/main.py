file = open('zen.txt', 'r')
text = []
for i_elem in file:
    text.append(i_elem)
file.close()

for string in reversed(text):
    print(string, end='')

# TODO между первой и второй строкой отсутствует перенос:
# Namespaces are one honking great idea -- let's do more of those!If the implementation is easy to explain, it may be a good idea.
# If the implementation is hard to explain, it's a bad idea.
# TODO в код нужно добавить обработку для этого случая,
#  чтобы каждое предложение отображалось на новой строке
