class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(', '}':'{', ']':'['}
        stack = []

        for char in s:

            if char in hashmap.values():
                stack.append(char)

            elif char in hashmap.keys():
                if stack:
                    if stack[-1] != hashmap[char]:
                        return False
                    else:
                        stack.pop()
                else:
                    return False

        return len(stack) == 0