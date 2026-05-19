class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        i, step = 0, 0
        queue = deque([(i, step)])
        visited = {i}

        group = {}
        for i, val in enumerate(arr):
            if not val in group:
                group[val] = [i]
            else:
                group[val].append(i)

        while queue:
            i, step = queue.popleft()

            if i == n - 1:
                return step

            if (ni:= i + 1) < n and not ni in visited:
                queue.append((ni, step + 1))
                visited.add(ni)

            if 0 <= (ni:= i - 1) and not ni in visited:
                queue.append((ni, step + 1))
                visited.add(ni)

            for j in group[arr[i]]:
                if i != j and not j in visited:
                    queue.append((j, step + 1))
                    visited.add(j)
            group[arr[i]] = []

        return -1