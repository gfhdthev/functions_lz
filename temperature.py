user_input = int(input('Введите температуру в Цельсиях: '))

#функция перевода цельсия в фарингейты
def farin(a: int) -> int:
    return a*9/5+32

print(farin(user_input))