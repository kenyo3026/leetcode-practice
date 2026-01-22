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

                value = dfs(factor, denom, visited)
                if value != -1:
                    return graph[numer][factor] * value

            return -1

        answers = []
        for numer, denom in queries:
            ans = dfs(numer, denom, set())
            answers.append(ans)

        return answers