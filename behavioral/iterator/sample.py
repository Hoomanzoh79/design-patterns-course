class FibbonachiIterator:
    def __init__(self,max,a = 0,b = 1):
        self.max = max
        self.a = a
        self.b = b
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.a > self.max:
            raise StopIteration
        else:
            current = self.a
            self.a, self.b = self.b, self.a + self.b
            return current

class FibbonachiSequence:
    def __init__(self,max):
        self.max = max
    
    def __iter__(self):
        return FibbonachiIterator(self.max)

# However,in python,the best way would be using a generator(there is no need to create an iterator) 
# (could be a simple function but a class is preffered here)
class FibbonachiSequenceGenerator:
    def __init__(self,max,a = 0,b = 1):
        self.max = max
        self.a = a
        self.b = b
    
    def __iter__(self):
        a, b = self.a, self.b
        while a <= self.max:
            yield a
            a, b = b, a + b

if __name__ == "__main__":
    for num in FibbonachiSequence(100):
        print(num,end = " ")
    print("\nSame result using generator:")
    for num in FibbonachiSequenceGenerator(100):
        print(num,end = " ")
