class Calculator:
    class ZeroDivisionError(Exception):
        pass

    class NegativePowerError(Exception):
        pass

    def add(self, a, b):
        try:
            result = a + b
        except TypeError:
            return "Ошибка: Недопустимые операнды для сложения."
        return result

    def subtract(self, a, b):
        try:
            result = a - b
        except TypeError:
            return "Ошибка: Недопустимые операнды для вычитания."
        return result

    def multiply(self, a, b):
        try:
            result = a * b
        except TypeError:
            return "Ошибка: Недопустимые операнды для умножения."
        return result

    def divide(self, a, b):
        try:
            result = a / b
        except TypeError:
            return "Ошибка: Недопустимые операнды для деления."
        except ZeroDivisionError:
            return "Ошибка: Деление на ноль."
        return result

    def power(self, a, b):
        try:
            if b < 0:
                raise self.NegativePowerError("Нельзя возводить число в отрицательную степень.")
            result = a ** b
        except TypeError:
            return "Ошибка: недопустимые операнды для возведения в степень."
        except self.NegativePowerError as e:
            return f"Ошибка: {e}"
        return result

    def sqrt(self, a):
        try:
            result = a ** 0.5
        except TypeError:
            return "Ошибка: недопустимый операнд для квадратного корня."
        except ValueError:
            return "Ошибка: невозможно вычислить квадратный корень из отрицательного числа."
        return result

calculator = Calculator()
print(calculator.add(2, 3))
print(calculator.subtract(5, 3))
print(calculator.multiply(2, 4))
print(calculator.divide(10, 2))
print(calculator.divide(10, 0))
print(calculator.divide("a", "b"))
print(calculator.power(2, 3))
print(calculator.power(2, -3))
