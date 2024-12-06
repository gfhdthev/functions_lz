user_input = float(input('Введите число: '))

#функция определяет четное ли число
def chet(a: float) -> bool:
    if a//1%2 == 0:
        return True
    else:
        return False
    
if chet(user_input) is True:
    print('Число четное')

elif chet(user_input) is False:
    print('Число нечетное')