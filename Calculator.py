from past.builtins import raw_input
import re


class Calculator:
    result = 0
    M = 0

    def add(self, x, y):
        self.result = x + y
        return self.result

    def subtract(self, x, y):
        self.result = x - y
        return self.result

    def multiply(self, x, y):
        self.result = x * y
        return self.result

    def divide(self, x, y):
        if y == 0:
            self.result = 0
        else:
            self.result = x / y

        return self.result

    def pow(self, x, y):
        self.result = x**y

        return self.result

    def sqrt(self, x, y):
        self.result = x ** (1/y)

        return self.result

    def save_result(self, result):
        self.M = result

    def validate_input(self, numbers):
        if len(numbers) != 2:
            print('Expression should contain only 2 numbers!')
            return 0, 0, False

        try:
            n1 = float((numbers[0]))
            n2 = float((numbers[1]))
        except ValueError:
            print("When I ask for a number, give me a number!")
            return 0, 0, False
        else:
            return n1, n2, True

    def calculate(self, expression):

        if 'M' in expression and any(x in expression for x in '+-*/'):
            expression = expression.replace('M', str(self.M))
            self.calculate(expression)

        elif '+' in expression:
            numbers = expression.split('+')
            n1, n2, validation_state = self.validate_input(numbers)
            if not validation_state:
                return False

            calculator.add(n1, n2)
            print(calculator.result)

        elif '-' in expression:
            numbers = expression.split('-')
            n1, n2, validation_state = self.validate_input(numbers)
            if not validation_state:
                return False

            calculator.subtract(n1, n2)
            print(calculator.result)

        elif '**' in expression:
            numbers = expression.split('**')
            n1, n2, validation_state = self.validate_input(numbers)
            if not validation_state:
                return False

            calculator.pow(n1, n2)
            print(calculator.result)

        elif '*' in expression:
            numbers = expression.split('*')
            n1, n2, validation_state = self.validate_input(numbers)
            if not validation_state:
                return False

            calculator.multiply(n1, n2)
            print(calculator.result)

        elif '//' in expression:
            numbers = expression.split('//')
            n1, n2, validation_state = self.validate_input(numbers)
            if not validation_state:
                return False

            calculator.sqrt(n1, n2)
            print(calculator.result)

        elif '/' in expression:
            numbers = expression.split('/')
            n1, n2, validation_state = self.validate_input(numbers)
            if not validation_state:
                return False

            calculator.divide(n1, n2)
            print(calculator.result)

        elif 'M' in expression:
            calculator.save_result(calculator.result)
            print(calculator.M)
            return self.M

        else:
            print('Enter correct expression!')


calculator = Calculator()

while True:
    expression = raw_input("Enter expression: ")
    calculator.calculate(expression)
