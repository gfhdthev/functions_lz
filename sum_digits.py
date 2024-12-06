user_input = str(input('Введите список чисел: '))

#функция суммы цифр
def sum(b: str) -> int:
    s = 0

    for i in b:
        i = int(i)
        s += i
    return s

print('Сумма всех цифр вашего числа:', sum(user_input))