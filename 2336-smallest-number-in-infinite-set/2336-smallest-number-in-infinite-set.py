class SmallestInfiniteSet:

    def __init__(self):
        self.i = 1
        self.add_heap = []

    def popSmallest(self) -> int:
        if self.add_heap and self.add_heap[0] < self.i:
            return heapq.heappop(self.add_heap)
        else:
            self.i += 1
            return self.i - 1

    def addBack(self, num: int) -> None:
        if num < self.i and not num in set(self.add_heap):
            heapq.heappush(self.add_heap, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)