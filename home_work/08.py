# Сделать программу в виде функций в которой нужно будет угадывать число.
def game():
    global number
    import random
    num = random.randint(1, 99)
    attempts = 0
    print('Отгадайте число между 1 и 99.')
    while attempts < 5:
        number = int(input('Введите число: '))
        attempts += 1
        if number < num:
            print('Ваше число меньше загаданного.')
        if number > num:
            print('Ваше число больше загаданного.')
        if number == num:
            break
    if number == num:
        print('Вы угадал число {0}, количество попыток {1}'.format(num, attempts))
    else:
        print('Вы не угадал число! Загаданное число {0}'.format(num))
game()
while True:
    question = input("Желаете повторить? (Д/Н)\n")
    if question.upper() in ('Д', 'Y'):
        game()
    elif question.upper() in ('Н', 'N'):
        print('Спасибо, до встречи')
        break
