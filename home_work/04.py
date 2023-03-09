# exercise №1
name_1, name_2 = input('Введите имя и фамилию: ').split()
name_a = '%s %s'%(name_2, name_1)
name_b = ' {} {}'.format((name_1).upper(), (name_2).title())
name_c = f'!{name_1} {name_2}?'
file_1= open('test.txt', 'w')
print(name_1, name_2, end='<<<>>>', file=file_1)
print(name_a, name_b, name_c, sep='<<<>>>', file=file_1)
file_1.close()


