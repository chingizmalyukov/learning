import re

text = """ Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, 
nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. 
Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate 
"""
patern = r'\b\w{4}\b'
solution = re.findall(patern, text)
print(solution)
# если я не присваиваю патерн переменной, а сразу его вбиваю в функцию, то она ничего не находит
# solution = re.findall(r'\\b\\w{4}\\b', text), почему так?
