import requests
import json

data = requests.get('https://breakingbadapi.com/api/deaths')
json_data = json.loads(data.text)

episodes_count = dict()

for i_death in json_data:
    value = (i_death['season'], i_death['episode'])

    if episodes_count.get(value):
        episodes_count[value] += i_death['number_of_deaths']
    else:
        episodes_count[value] = i_death['number_of_deaths']

solution = max(episodes_count, key=episodes_count.get)
print(solution)
with open('death_count.txt', 'w') as file:
    file.write(f'(Сезон, Серия): {solution}, кол-во смертей: {episodes_count[solution]}\n')

# Чтобы решить данную задачу - нужен VPN!!!!!!
# TODO сожалею об этом факте. Уже передала создателям курса.
#  И в ответе ошибка. Верно 2 сезон, 13 эпизод, в котором количество смертей - 167
#  Это 'Unnamed passengers on the Wayfarer 515 and JM 21 flights'
# поправил
