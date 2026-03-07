class CRUD:
    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


# take input from terminal
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# create object
obj = CRUD()

add = obj.addition(a, b)
sub = obj.subtraction(a, b)
mul = obj.multiplication(a, b)
div = obj.div(a, b)

print("\nResults")
print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)