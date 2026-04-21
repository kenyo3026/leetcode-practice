class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(', '}':'{', ']':'['}
        stack = []

        for char in s:

            if char in hashmap.values():
                stack.append(char)

            if char in hashmap.keys():
                if stack and stack[-1] == hashmap[char]:
                    stack.pop()
                    continue
                else:
                    return False

        return len(stack) == 0