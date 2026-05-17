class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        queue = deque([start])
        visited = {start}

        while queue:
            idx = queue.popleft()

            if arr[idx] == 0:
                return True

            for next_idx in (idx - arr[idx], idx + arr[idx]):

                if (0 <= next_idx < n) and not next_idx in visited:
                    queue.append(next_idx)
                    visited.add(next_idx)

        return False