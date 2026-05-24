class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        for prereq, course in prerequisites:
            graph[course].append(prereq)

        states = [0] * numCourses

        def dfs(course):
            if states[course] == 1:
                return False
            elif states[course] == 2:
                return True

            states[course] = 1

            for prereq in graph[course]:
                if not dfs(prereq):
                    return False

            states[course] = 2
            return True            

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True