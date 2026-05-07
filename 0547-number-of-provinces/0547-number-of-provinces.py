class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        provinces_so_far = 0

        def dfs(city_id):
            visited.add(city_id)

            for neighbor_id in range(n):

                if neighbor_id == city_id:
                    continue

                if neighbor_id in visited:
                    continue

                if isConnected[city_id][neighbor_id] == 1:
                    dfs(neighbor_id)


        for city_id in range(n):
            if not city_id in visited:
                provinces_so_far += 1
                dfs(city_id)

        return provinces_so_far