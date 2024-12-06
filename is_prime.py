user_input = int(input('Введите число: '))

#функция вычисления площади
def prost(b: int) -> bool:
    for i in range(2, b+1):
        if b%i == 0 and b != i: #ищем числа, на которое делится вводное число, и которое не равно ему
            return False

        elif b%i == 0 and b == i: #а если цикл доходит до найшего вводного числа, то, значит, оно простое
            return True
        
if prost(user_input) is True:
    print('Ваши число простое')

else:
    print('Ваши число составное')