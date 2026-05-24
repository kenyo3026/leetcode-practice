class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degress = [0 for i in range(numCourses)]
        graph = [[] for i in range(numCourses)]

        for prereq, course in prerequisites:
            in_degress[course] += 1
            graph[prereq].append(course)

        topos = []
        queue = deque([i for i in range(numCourses) if in_degress[i] == 0])

        while queue:
            prereq = queue.popleft()
            topos.append(prereq)

            for course in graph[prereq]:
                in_degress[course] -= 1

                if in_degress[course] == 0:
                    queue.append(course)

        return topos.__len__() == numCourses