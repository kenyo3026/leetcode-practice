class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        queue = deque([start])
        visited = set()

        while queue:
            idx = queue.popleft()

            for next_idx in (idx - arr[idx], idx + arr[idx]):

                if not (0 <= next_idx < n):
                    continue

                if next_idx in visited:
                    continue

                if arr[next_idx] == 0:
                    return True

                queue.append(next_idx)
                visited.add(next_idx)

        return False