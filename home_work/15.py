str_1 = b'r\xc3\xa9sum\xc3\xa9'
str_1 = str_1.decode()
Latin1_b_str = str_1.encode('Latin1')
Latin1_s_str = Latin1_b_str.decode('Latin1')
print(f'Декодированная строка в кодировке по умолчанию: {str_1}')
print(f"Байтовая строка в кодировке 'Latin1': {Latin1_b_str}")
print(f"Декодированная строка в кодировке 'Latin1': {Latin1_s_str}")
