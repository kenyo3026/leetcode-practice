class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        queue = deque([start])
        visited = {start}

        while queue:
            i = queue.popleft()

            if arr[i] == 0:
                return True

            for ni in [i+arr[i], i-arr[i]]:
                if 0 <= ni < n and not ni in visited:
                    queue.append(ni)
                    visited.add(ni)

        return False