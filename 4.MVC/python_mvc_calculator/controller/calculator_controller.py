from model.calculator import Calculator

class CalculatorController:

    def __init__(self):
        self.model = Calculator()

    def add(self, a, b):
        return self.model.addition(a, b)

    def sub(self, a, b):
        return self.model.subtraction(a, b)

    def mul(self, a, b):
        return self.model.multiplication(a, b)

    def div(self, a, b):
        return self.model.division(a, b)