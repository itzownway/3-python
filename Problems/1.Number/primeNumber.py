class primeNumber:


    def isPrime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    

obj = primeNumber()
number = int(input("Enter a number: "))
if obj.isPrime(number):
    print(f"{number} is a prime number.")
else:    print(f"{number} is not a prime number.")