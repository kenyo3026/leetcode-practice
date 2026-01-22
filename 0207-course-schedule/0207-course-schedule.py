class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degrees = [0 for _ in range(numCourses)]
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            in_degrees[course] += 1
            graph[prereq].append(course)

        topo_sorted = []
        queue = [course for course in range(numCourses) if in_degrees[course] == 0]

        while queue:
            node = queue.pop()
            topo_sorted.append(node)

            for neighbor in graph[node]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)

        return len(topo_sorted) == numCourses