class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:

        graph = {i:[] for i in range(n)}
        for u, v in invocations:
            graph[u].append(v)

        queue = deque([k])
        visited = set([k])
        while queue:
            u = queue.popleft()

            for v in graph[u]:
                if v in visited:
                    continue
                queue.append(v)
                visited.add(v)

        suspicious = visited

        # check if ANY external method calls into the suspicious group
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                return list(range(n))  # cannot remove the group at all

        return [i for i in range(n) if i not in suspicious]
