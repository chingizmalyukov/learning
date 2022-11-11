import requests
import json

data = requests.get('https://breakingbadapi.com/api/deaths')
json_data = json.loads(data.text)
episodes_count = dict()

for i_death in json_data:
    value = (i_death['season'], i_death['episode'])

    if episodes_count.get(value):
        episodes_count[value] += 1
    else:
        episodes_count[value] = 1

solution = max(episodes_count, key=episodes_count.get)
print(solution)
with open('death_count.txt', 'w') as file:
    file.write(f'(Сезон, Серия): {solution}, кол-во смертей: {episodes_count[solution]}\n')

# Чтобы решить данную задачу - нужен VPN!!!!!!
