class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(', '}':'{', ']':'['}

        stack = []
        for i in range(len(s)):

            if s[i] in hashmap.values():
                stack.append(s[i])

            else:
                if stack and stack[-1] == hashmap[s[i]]:
                    stack.pop()
                else:
                    return False

        return True