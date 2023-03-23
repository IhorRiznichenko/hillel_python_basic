line1 = input("Введите первую строку: ")
line2 = input("Введите вторую строку: ")
line3 = input("Введите третью строку: ")
line4 = input("Введите четвертую строку: ")

with open('file.txt', 'w') as file:
    file.write(line1 + '\n')
    file.write(line2 + '\n')

with open('file.txt', 'a') as file:
    file.write(line3 + '\n')
    file.write(line4 + '\n')

