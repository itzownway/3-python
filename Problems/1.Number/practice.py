class Practice:

    n1 = 0
    n2 = 1

    def fibonacci(self, num):
        
        for i in range(num):
            n3 = self.n1 + self.n2
            print(self.n1)
            self.n1 = self.n2
            self.n2 = n3


obj = Practice()
obj.fibonacci(10)