class RecentCounter:

    def __init__(self):
        self.internal = 3000
        self.queue = deque([])

    def ping(self, t: int) -> int:
        while self.queue:
            if self.queue[0] < t - 3000:
                self.queue.popleft()
            else:
                break
        self.queue.append(t)
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)