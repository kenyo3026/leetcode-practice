class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for course in range(numCourses)]
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visited = [0] * numCourses

        def dfs(node): # treat as check is cycle or not
            if visited[node] == 1:
                return True
            elif visited[node] == 2:
                return False

            visited[node] = 1

            for neighbor in graph[node]:
                if dfs(neighbor):
                    return True

            visited[node] = 2
            return False

        for course in range(numCourses):
            if dfs(course):
                return False
        return True