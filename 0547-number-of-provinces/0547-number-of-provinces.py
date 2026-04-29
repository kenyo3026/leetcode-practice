class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        province_so_far = 0

        def dfs(city_id):
            visited.add(city_id)

            for neighbor_id in range(n):
                _is_connected = isConnected[city_id][neighbor_id]

                if _is_connected and not neighbor_id in visited:
                    dfs(neighbor_id)

        for city_id in range(n):
            if not city_id in visited:
                province_so_far += 1
                dfs(city_id)

        return province_so_far