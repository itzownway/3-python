x = y = z = "orange"
print(x)
print(y)
print(z)



fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)    
print(y)
print(z)


x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


# Global variables

x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()
print("Python is " + x)