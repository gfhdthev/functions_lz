user_input = int(input('Введите радиус: '))

#функция вычисления площади
def plo(r: int) -> int:
    return 3.14*r**2
#функция вычисления длинв окружности
def ockr(r: int) -> int:
    return 2*3.14*r

print('Длина окружности:', ockr(user_input))
print('Площадь окружности:', plo(user_input))