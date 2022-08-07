N = int(input("Кол-во друзей: "))
K = int(input("Долговых расписок: "))
friends_list = []

for _ in range(N):
    friends_list.append(0)

for number in range(K):
    print("\n", number + 1, "-я расписка: ")
    creditor = int(input("Кому: "))
    borrower = int(input("От кого: "))
    money = int(input("Сколько: "))
    friends_list[borrower - 1] += money
    friends_list[creditor - 1] -= money

print("Баланс друзей: ")
for index in range(len(friends_list)):
    print(index + 1, ": ", friends_list[index])