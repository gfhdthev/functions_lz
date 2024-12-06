user_input = str(input('Введите строку: '))

#функция вычисления площади
def palindrom(b: str) -> bool:
    b.lower()

    for i in b: #проверяем всю строку на пробелы
        if i == ' ': 
            b = b[:b.index(i)] + b[b.index(i)+1:] #вырезаем каждый пробел

    b = b.split()

    for i in range(len(b)//2):
        if b[i] != b[-(i+1)]:
            return False
        
    return True

if palindrom(user_input) is True:
    print('Ваша строка палиндром')

else:
    print('Ваша строка не палиндром')