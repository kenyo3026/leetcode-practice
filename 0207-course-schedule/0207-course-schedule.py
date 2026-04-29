class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graphs = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graphs[prereq].append(course)

        # 0 = unvisited
        # 1 = visiting (currently in DFS stack)
        # 2 = visited (fully processed, no cycle)
        states = [0] * numCourses

        def dfs(course):
            if states[course] == 1:
                return False
            if states[course] == 2:
                return True

            states[course] = 1

            for neighbor in graphs[course]:
                if not dfs(neighbor):
                    return False

            states[course] = 2
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True