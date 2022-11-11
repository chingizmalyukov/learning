import re

text = """ Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, 
nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. 
Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate 
"""
patern = r'\b\w{4}\b'
# solution = re.findall(patern, text)
solution = re.findall(r'\b\w{4}\b', text)
print(solution)
# если я не присваиваю паттерн переменной, а сразу его вбиваю в функцию, то она ничего не находит
# solution = re.findall(r'\\b\\w{4}\\b', text), почему так?
# NOTE потому, что экранировать символы слэшей не нужно
#  Обратите внимание на код в 10 строке - он работает так же, как и Ваш исходный на 9 строке
#  Символ r вначале строке так же означает, что строка "сырая" (row string)
#  то есть все специальные символы в ней экранированы по-умолчанию
