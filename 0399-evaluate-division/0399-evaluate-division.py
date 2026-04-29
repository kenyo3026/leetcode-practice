class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graphs = {}
        for (numer, denom), value in zip(equations, values):
            if not numer in graphs:
                graphs[numer] = {}
            graphs[numer][denom] = value

            if not denom in graphs:
                graphs[denom] = {}
            graphs[denom][numer] = 1 / value

        def dfs(numer, denom, visited):
            if not numer in graphs or not denom in graphs:
                return -1

            if denom in graphs[numer]:
                return graphs[numer][denom]

            visited.add(numer)

            for factor in graphs[numer]:
                if factor in visited:
                    continue

                value = dfs(factor, denom, visited)
                if value != -1:
                    return graphs[numer][factor] * value

            return -1

        res = []
        for numer, denom in queries:
            res.append(dfs(numer, denom, set()))
        return res