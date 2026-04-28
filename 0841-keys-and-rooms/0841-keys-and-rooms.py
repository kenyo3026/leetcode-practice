class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(key):
            visited.add(key)

            next_keys = rooms[key]
            for next_key in next_keys:

                if next_key in visited:
                    continue

                dfs(next_key)

        dfs(0)
        return len(visited) == len(rooms)