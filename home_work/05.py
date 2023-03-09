while True:
    name = input('Привет, как тебя зовут?\n')
    age = input('Сколько тебе лет?\n')
    if not age.isdigit() or int(age)<=0:
        print('Ошибка, повторите ввод')
    elif int(age) >0 and int(age)<10:\
        print(f'Привет, шкет {name}')
    elif int(age)>=10 and int(age) <=18:
        print(f'Как жизнь {name}?')
    elif int(age)>18 and int(age) <100:
        print(f'Что желаете {name}')
    else:
        print(f'{name}, вы лжете - в наше время столько не живут...')
    question = input("Желаете выйти? (Д/Y)\n")
    if question == 'д' or question == 'Д' or question == 'y' or question == 'Y':
        break

