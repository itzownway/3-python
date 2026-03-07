from model.calculator import Calculator

class CalculatorController:

    def __init__(self):
        self.calc = Calculator()

    def calculate(self, operation, a, b):

        if operation == "add":
            return self.calc.addition(a, b)

        if operation == "sub":
            return self.calc.subtraction(a, b)

        if operation == "mul":
            return self.calc.multiplication(a, b)

        if operation == "div":
            return self.calc.division(a, b)