user_input = int(input('Введите число: '))

#функция определяет четное ли число
def chet(a: int) -> bool:
    if a%2 == 0:
        return True
    else:
        return False
    
if chet(user_input) is True:
    print('Число четное')

elif chet(user_input) is False:
    print('Число нечетное')