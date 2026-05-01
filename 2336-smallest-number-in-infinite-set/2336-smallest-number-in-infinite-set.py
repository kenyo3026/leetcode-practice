class SmallestInfiniteSet:

    def __init__(self):
        self.i = 1
        self.add_heap = []
        self.add_set = set()

    def popSmallest(self) -> int:
        if self.add_heap and self.add_heap[0] < self.i:
            num_to_pop = heapq.heappop(self.add_heap)
            self.add_set.remove(num_to_pop)
            return num_to_pop
        else:
            num_to_pop = self.i
            self.i += 1
            return num_to_pop

    def addBack(self, num: int) -> None:
        if num < self.i and not num in self.add_set:
            heapq.heappush(self.add_heap, num)
            self.add_set.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)