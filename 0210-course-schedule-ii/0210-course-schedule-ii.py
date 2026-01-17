class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for i in range(numCourses)]
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visited = [0] * numCourses
        topo_sorted = []

        def dfs(node): # treat as check has cycle or not
            if visited[node] == 1:
                return True
            elif visited[node] == 2:
                return False

            visited[node] = 1

            for neighbor in graph[node]:
                if dfs(neighbor):
                    return True

            topo_sorted.append(node)
            visited[node] = 2
            return False

        for course in range(numCourses):
            if dfs(course):
                return []
        return topo_sorted