import csv
import json
import random

with open('my_dict.json', 'r') as file:
    my_dict = json.load(file)

operators = ['095', '066', '098', '096', '050', '097']

for key in my_dict:
    if random.random() < 0.75:
        operator = random.choice(operators)
        phone_number = operator + ''.join(random.choice('0123456789') for _ in range(7))
    else:
        phone_number = ''
    my_dict[key] = list(my_dict[key])
    my_dict[key].extend([phone_number])
    my_dict[key] = tuple(my_dict[key])

with open('my_dict.csv', 'w', newline='', encoding='utf-8') as write_file:
    writer = csv.writer(write_file)
    writer.writerow(['ID', 'Имя', 'Возраст', 'Телефон'])
    for key in my_dict:
        row = [key] + list(my_dict[key])
        writer.writerow(row)

