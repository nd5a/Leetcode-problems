# Product of the last K numbers

class ProductOfNumbers:

    def __init__(self):
        self.stack = []
        self.ones = 0
        self.counter = 0
    
    def add(self, num):
        self.counter += 1

        if num == 0:
            self.stack = []
            self.ones =0
            return
        if num == 1:
            self.ones += 1
            return
        self.stack.append((num, self.counter)) 

    def getProduct(self, k):
        if len(self.stack) + self.ones < k:
            return 0
        product = 1
        for index in range(len(self.stack) - 1, -1, -1):
            x, c = self.stack[index]

            if self.counter - c >= k:
                return product
            product *= x
        return product


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)