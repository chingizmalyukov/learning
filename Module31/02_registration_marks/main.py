import re

text = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

privat_patern = r'\b\w\d{3}\w{2}\d{2,3}'
taxi_patern = r'\b\w{2}\d{3}\d{2,3}'

print('Список номеров частных автомобилей:', re.findall(privat_patern, text))
print('Список номеров такси:', re.findall(taxi_patern, text))
