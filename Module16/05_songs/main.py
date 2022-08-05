violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

count = int(input('Сколько песен выбрать? '))
time = 0
step = 0

while step != count:
    print('Название', step + 1,'-й песни:', end=' ')
    name = input()
    for track in violator_songs:
        if track[0] == name:
            time += track[1]
            step += 1
            break
print('\nОбщее время звучания песен:', round(time,2), 'минуты')