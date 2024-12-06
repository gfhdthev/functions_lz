user_input = str(input('Введите список чисел: '))

#функция вычисления площади
def sum(b: str) -> int:
    s = 0
    b = b.split()

    for i in b:
        i = int(i)
        s += i
    return s

print('Сумма всех чисел вашего списка:', sum(user_input))