user_input = str(input('Введите строку: '))

#функция узнаем является ли число палиндромом
def palindrom(b: str) -> bool:
    b.lower()

    for i in b: #проверяем всю строку на пробелы
        if i == ' ': 
            b = b[:b.index(i)] + b[b.index(i)+1:] #вырезаем каждый пробел

    b = b.split()

    for i in range(len(b)//2):
        if b[i] != b[-(i+1)]:
            return False #если два последних числа не совпадают, то выводит False
        
    return True #если жо этого не вывело False, то выведет True

if palindrom(user_input) is True:
    print('Ваша строка палиндром')

else:
    print('Ваша строка не палиндром')