class Solution:
    def smallestSubsequence(self, s: str) -> str:
        char_stat = {}
        for char in s:
            char_stat[char] = char_stat.get(char, 0) + 1

        stack, stack_set = [], set()
        for char in s:
            char_stat[char] -= 1

            if char in stack_set:
                continue

            while stack and stack[-1] > char and char_stat[stack[-1]] > 0:
                stack_set.remove(stack.pop())

            stack.append(char)
            stack_set.add(char)

        return "".join(stack)