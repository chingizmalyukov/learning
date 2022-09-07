import zipfile

symbols_dict = dict()

archive = "./voyna-i-mir.zip"
directory_to_extract_to = "./"
with zipfile.ZipFile(archive, 'r') as zip_file:
    zip_file.extractall(directory_to_extract_to)

file = open('voyna-i-mir.txt', 'r', encoding='utf-8')
for string in file:
    for letter in list(string):
        if letter in symbols_dict:
            symbols_dict[letter] += 1
        else:
            symbols_dict[letter] = 1
file.close()

sorted_dictionary = dict((sorted(symbols_dict.items(), key=lambda x: x[1])))

file = open('solution.txt', 'a')
for letter, amount in sorted_dictionary.items():
    file.write(str(letter))
    file.write(' ')
    file.write(str(amount))
    file.write('\n')
    print(letter, amount)
file.close()
