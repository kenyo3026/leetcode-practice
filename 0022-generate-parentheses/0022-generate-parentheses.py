class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        gened_parentheses = []

        def dfs(part_of_parentheses:str, op_so_far:int, cl_so_far:int):

            if op_so_far == n and cl_so_far == n:
                gened_parentheses.append(part_of_parentheses)
                return

            if op_so_far < n:
                dfs(part_of_parentheses+'(', op_so_far+1, cl_so_far)

            if cl_so_far < op_so_far:
                dfs(part_of_parentheses+')', op_so_far, cl_so_far+1)

        dfs("", 0, 0)
        return gened_parentheses