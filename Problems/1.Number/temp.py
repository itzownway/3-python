class celcius:
   def fahrenheit_to_celsius(fahrenheit):
     return (fahrenheit - 32) * 5 / 9


  
temp = float(input("Enter temperature in Fahrenheit: "))
celsius = celcius.fahrenheit_to_celsius(temp)
print(f"{temp} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius.")