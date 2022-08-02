def summ(n):
    summ_numbers = 0
    while n != 0:
        summ_numbers += n % 10
        n //= 10
    return summ_numbers
def count(n):
    count_numbers = 0
    while n != 0:
        n //= 10
        count_numbers += 1
    return count_numbers

n = int(input('Введите N: '))
print('')
print('Сумма чисел:', summ(n))
print('Количество цифр в числе:', count(n))
print('Разность суммы и количества цифр:', summ(n)-count(n))

#логично было бы сделать все в одной функции, просто добавить счетчик итераций цикла.
#и его использовать, как кол-во чисел. НО в ТЗ просили другое =)