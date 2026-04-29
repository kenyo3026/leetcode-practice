class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(key):
            visited.add(key)

            for key in rooms[key]:
                if not key in visited:
                    dfs(key)

        dfs(0)
        return len(visited) == len(rooms)