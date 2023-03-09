value = 1
result = 0
num = int(input("Введите число: "))

for i in range(value, num+1):
    if i % 3 != 0:
        result += i ** 3

print(f'result:  {result}')

result = 0
while num > 0:
    if num % 3 != 0:
        result += num ** 3
    num -= 1

print(f'result:  {result}')
