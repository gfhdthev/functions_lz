from math import fabs

user_input = str(input('Введите список чисел: '))
user_input = user_input.split()

def f_max(b: list) -> int:
    return max(b)

def f_min(b: list) -> int:
    return min(b)

def f_mid(b: list) -> int:
    #находим среднее значение
    sred = 0
    for i in b:
        i = int(i)
        sred += i
    sred = sred / len(b)

    a = abs(int(b[0]) - sred) #устанавливыаем изначальное значение, с которым будем сравнивать
    chislo = b[0] #если не найдет число юлиже, то выведет его

    for i in b:
        i = int(i)
        if abs(i - sred) < a: #сравниваем с установленным значением
            a = abs(i - sred)
            chislo = i #если меньше, то присваиваем новое

    return chislo

print('Максимальное число:', f_max(user_input))
print('Минимальное число:', f_min(user_input))
print('Среднее число:', f_mid(user_input))