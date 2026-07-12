class SummaryRanges:

    def __init__(self):
        self.parents = {}
        self.starts = {}
        self.ends = {}

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root != y_root:
            self.parents[y] = x_root
            self.starts[x_root] = min(self.starts[x_root], self.starts[y_root])
            self.ends[x_root] = max(self.ends[x_root], self.ends[y_root])

    def addNum(self, value: int) -> None:
        if value in self.parents:
            return

        self.parents[value] = value
        self.starts[value] = value
        self.ends[value] = value

        if value-1 in self.parents:
            self.union(value-1, value)
        if value+1 in self.parents:
            self.union(value, value+1)

    def getIntervals(self) -> List[List[int]]:
        roots = set(self.find(x) for x in self.parents)
        intervals = [[self.starts[root], self.ends[root]] for root in roots]
        intervals.sort()
        return intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()