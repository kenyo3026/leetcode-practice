class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0 for i in range(numCourses)]
        graph = [[] for i in range(numCourses)]
        for prereq, course in prerequisites:
            in_degree[course] += 1
            graph[prereq].append(course)

        topo_count = 0
        queue = deque([course for course in range(numCourses) if in_degree[course] == 0])
        while queue:
            prereq = queue.popleft()
            topo_count += 1

            for course in graph[prereq]:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    queue.append(course)

        return topo_count == numCourses