class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        in_degrees = [0 for _ in range(numCourses)]

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degrees[course] += 1

        queue = [course for course in range(numCourses) if in_degrees[course] == 0]
        topo_sorted = []

        while queue:
            node = queue.pop()
            topo_sorted.append(node)

            for neighbor in graph[node]: # unlock progressively
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)

        return len(topo_sorted) == numCourses