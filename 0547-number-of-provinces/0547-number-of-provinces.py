class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        n_of_provinces = 0
        visited = set()

        def dfs(city_id):
            visited.add(city_id)

            for neighbor_city_id, is_connected in \
                enumerate(isConnected[city_id]):
                if is_connected and not neighbor_city_id in visited:
                    dfs(neighbor_city_id)

        for i in range(n):
            if not i in visited:
                n_of_provinces += 1
                dfs(i)

        return n_of_provinces