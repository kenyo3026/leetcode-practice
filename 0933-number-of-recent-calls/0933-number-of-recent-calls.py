class RecentCounter:

    def __init__(self):
        self.time_frame = 3000
        self.queue = deque([])

    def ping(self, t: int) -> int:
        while self.queue:
            if self.queue[0] < t - self.time_frame:
                self.queue.popleft()
            else:
                break

        self.queue.append(t)
        return len(self.queue)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)