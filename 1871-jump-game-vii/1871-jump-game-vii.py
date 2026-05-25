class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[-1] != '0':
            return False

        queue = deque([0])
        visited = 0

        while queue:
            i = queue.popleft()
            if i == n - 1:
                return True

            start = max(i + minJump, visited)
            end = min(i + maxJump + 1, n)

            queue.extend([i for i in range(start, end) if s[i] == '0'])

            visited = max(visited, end)

        return False