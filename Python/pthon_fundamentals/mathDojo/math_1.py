class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for n in nums:
            self.result += n
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for n in nums:
            self.result -= n
        return self


# Create an instance
md = MathDojo()

# To test:
x = md.add(2).add(2, 5, 1).subtract(3, 2).result
print(x)  # output print 5

y = md.add(10).subtract(4, 1).add(3, 2, 1).result
print(y)  # output print 16
