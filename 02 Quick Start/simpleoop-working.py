#!/usr/bin/python3

# simple fibonacci series
# the sum of two elements defines the next set
class Fibonacci():  # class is like a blue print
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def series(self):
        while(True):
            yield(self.b) # create a infinite iterator
            self.a, self.b = self.b, self.a + self.b

f = Fibonacci(0, 1) # instantiation create an object(an instance of a class)
for r in f.series():
    if r > 100: break    
    print(r, end=' ')

