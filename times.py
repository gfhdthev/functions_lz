user_input = input('Введите время в формате часы-миннуты-секунды: ')

#перевод времени в секунды
def sec(a: str) -> int:
    a = a.split('-')

    return int(a[0])*60*60 + int(a[1])*60 + int(a[2])

print('Ваше время в секундах: ', sec(user_input))