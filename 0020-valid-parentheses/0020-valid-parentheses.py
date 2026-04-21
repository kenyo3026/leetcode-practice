class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(', '}':'{', ']':'['}
        stack = []

        for char in s:

            if char in hashmap.values():
                stack.append(char)

            elif stack and char in hashmap.keys():
                if stack[-1] != hashmap[char]:
                    return False
                else:
                    stack.pop()

            elif not stack and char in hashmap.keys():
                return False

        return len(stack) == 0