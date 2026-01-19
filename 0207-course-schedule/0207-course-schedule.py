class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Determines if all courses can be completed by detecting cycles in a directed graph
        using DFS with Three-Color Marking.

        State Definitions:
        - 0 (Unvisited): The node has never been inspected.
        - 1 (Visiting):  The node is currently in the recursion stack (processing started but not finished).
        - 2 (Visited):   The node and all its descendants have been fully processed and verified as safe.

        Key Logic:
        1. Cycle Detection (State == 1):
           If we encounter a node marked '1', it means we have looped back to an ancestor 
           in the current recursion path. This confirms a cycle exists (A -> B -> ... -> A).

        2. Pruning / Memoization (State == 2):
           If we encounter a node marked '2', it means this node was already checked in a 
           previous DFS iteration and proved safe. We return False immediately to skip 
           redundant computations (Optimization).
        """
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visited = [0] * numCourses

        def dfs(node):

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