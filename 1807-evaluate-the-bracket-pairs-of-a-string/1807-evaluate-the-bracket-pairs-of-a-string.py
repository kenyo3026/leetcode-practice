class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        n = len(s)
        knowledge = {key:value for key, value in knowledge}

        i, res = 0, []
        while i < n:
            if s[i] == '(':
                j = i + 1
                while j < n:
                    if s[j] == ')':
                        break
                    j += 1
                key = s[i+1:j]
                value = knowledge.get(key, '?')
                res.append(value)
                i = j
            else:
                res.append(s[i])
            i += 1

        return ''.join(res)
