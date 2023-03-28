import json

my_dict = {
    123456: ('Ihor', 31),
    234567: ('Lilya', 32),
    345678: ('Lera', 33),
    456789: ('Eve', 34),
    567890: ('Pavel', 35)
}
with open('my_dict.json', 'w') as write_file:
    json.dump(my_dict, write_file)
