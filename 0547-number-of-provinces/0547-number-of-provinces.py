class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        n = len(isConnected)
        provinces_so_far = 0

        def dfs(city_id):
            visited.add(city_id)

            for neighbor_city_id in range(n):

                if neighbor_city_id == city_id:
                    continue

                if neighbor_city_id in visited:
                    continue

                if isConnected[city_id][neighbor_city_id] == 1:
                    dfs(neighbor_city_id)

        for i in range(n):
            if not i in visited:
                provinces_so_far += 1
                dfs(i)

        return provinces_so_far