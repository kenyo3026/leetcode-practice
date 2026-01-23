class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for (numer, denom), value in zip(equations, values):
            graph[numer] = graph.get(numer, {})
            graph[numer][denom] = value

            graph[denom] = graph.get(denom, {})
            graph[denom][numer] = 1 / value


        def dfs(numer, denom, visited):

            if not numer in graph or not denom in graph:
                return -1

            if denom in graph[numer]:
                return graph[numer][denom]

            visited.add(numer)

            for factor in graph[numer]:

                if factor in visited:
                    continue

                res = dfs(factor, denom, visited)
                if res != -1:
                    return graph[numer][factor] * res

            return -1

        results = []
        for numer, denom in queries:
            res = dfs(numer, denom, set())
            results.append(res)

        return results