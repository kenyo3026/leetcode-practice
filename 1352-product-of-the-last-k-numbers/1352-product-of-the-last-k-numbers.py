class ProductOfNumbers:

    def __init__(self):
        self.n = 1
        self.prefixes = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.n = 1
            self.prefixes = [1]
        else:
            self.n += 1
            self.prefixes.append(self.prefixes[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= self.n:
            return 0
        return self.prefixes[-1] // self.prefixes[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)