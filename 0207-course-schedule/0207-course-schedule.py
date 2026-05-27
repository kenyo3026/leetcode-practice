class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0 for i in range(numCourses)]
        graph = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            in_degree[course] += 1
            graph[prereq].append(course)

        founds = 0
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        while queue:
            prereq = queue.popleft()
            founds += 1

            for course in graph[prereq]:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    queue.append(course)

        return founds == numCourses