def lowwest(num_list):
    lowwest_num = num_list[0]
    for num in num_list:
        if num < lowwest_num:
            lowwest_num = num
    return lowwest_num

skates_list = []
foot_list = []
solution = 0

count_skates = int(input('Кол-во коньков: '))

for i in range (count_skates):
    print('Размер', i+1, '-й пары:', end=' ')
    num = int(input())
    skates_list.append(num)

count_peoples = int(input('\nКол-во людей: '))
for i in range (count_peoples):
    print('Размер ноги', i+1, '-го человека:', end=' ')
    num = int(input())
    foot_list.append(num)
while True:
    if foot_list == [] or skates_list == []:
        break
    a = lowwest(foot_list)
    b = lowwest(skates_list)
    if b <= a:
        solution += 1
        foot_list.remove(lowwest(foot_list))
        skates_list.remove(lowwest(skates_list))
    else:
        break

print('\nНаибольшее кол-во людей, которые могут взять ролики:', solution)


