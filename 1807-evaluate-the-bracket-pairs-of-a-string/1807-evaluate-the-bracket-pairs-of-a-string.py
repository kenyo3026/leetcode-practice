class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        knowledge:dict = {key:value for key, value in knowledge}

        i, n = 0, len(s)
        res = []
        while i < n:
            if s[i] == "(":
                j = i + 1
                while j < n:
                    if s[j] == ")":
                        break
                    j += 1
                key = s[i+1:j]
                res.append(knowledge.get(key, "?"))
                i = j
            else:
                res.append(s[i])
            i += 1

        return "".join(res)