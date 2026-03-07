import tkinter as tk
from controller.calculator_controller import CalculatorController


class CalculatorView:

    def __init__(self, root):
        self.controller = CalculatorController()

        self.root = root
        self.root.title("MVC Calculator")

        tk.Label(root, text="First Number").pack()
        self.num1 = tk.Entry(root)
        self.num1.pack()

        tk.Label(root, text="Second Number").pack()
        self.num2 = tk.Entry(root)
        self.num2.pack()

        tk.Button(root, text="Add", command=self.add).pack()
        tk.Button(root, text="Subtract", command=self.sub).pack()
        tk.Button(root, text="Multiply", command=self.mul).pack()
        tk.Button(root, text="Divide", command=self.div).pack()

        self.result = tk.StringVar()
        tk.Label(root, textvariable=self.result).pack()

    def get_values(self):
        a = float(self.num1.get())
        b = float(self.num2.get())
        return a, b

    def add(self):
        a, b = self.get_values()
        self.result.set(self.controller.add(a, b))

    def sub(self):
        a, b = self.get_values()
        self.result.set(self.controller.sub(a, b))

    def mul(self):
        a, b = self.get_values()
        self.result.set(self.controller.mul(a, b))

    def div(self):
        a, b = self.get_values()
        self.result.set(self.controller.div(a, b))