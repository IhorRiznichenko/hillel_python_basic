def input_a(input_str):
    if input_str.isdigit():
        if int(input_str) == 0:
            return "Вы ввели ноль"
        elif int(input_str) > 0:
            return "Вы ввели положительное целое число: " + input_str
        else:
            return "Вы ввели отрицательное целое число: " + input_str
    else:
        try:
            num = float(input_str.replace(",", "."))
            if num < 0:
                return "Вы ввели отрицательное дробное число: " + str(num)
            else:
                return "Вы ввели положительное дробное число: " + str(num)
        except ValueError:
            return "Вы ввели не корректное число: " + input_str


while True:
    input_str = input("Введите число или 'выход', 'exit', 'quit', 'e' или 'q' для выхода:\n ").strip().lower()
    if input_str in ["выход", "exit", "quit", "e", "q"]:
        break
    else:
        print(input_a(input_str))

