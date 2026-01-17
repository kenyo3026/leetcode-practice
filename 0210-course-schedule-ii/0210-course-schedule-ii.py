class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        in_degrees = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degrees[course] += 1

        queue = [course for course in range(numCourses) if in_degrees[course] == 0]
        topo_sorted = []

        while queue:
            node = queue.pop()
            topo_sorted.append(node)

            for neighbor in graph[node]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)

        if len(topo_sorted) == numCourses:
            return topo_sorted
        return []