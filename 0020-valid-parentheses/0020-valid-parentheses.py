class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(', '}':'{', ']':'['}

        stack = []
        for char in s:
            if char in hashmap.values():
                stack.append(char)
            else:
                if stack and hashmap[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return not stack