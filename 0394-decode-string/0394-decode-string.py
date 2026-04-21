class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str, curr_num = '', 0

        for char in s:

            if char.isdigit():
                curr_num = (curr_num * 10) + int(char)

            elif char.isalpha():
                curr_str += char

            elif char == '[':
                stack.append((curr_str, curr_num))
                curr_str, curr_num = '', 0

            elif char == ']':
                prev_str, num = stack.pop()
                curr_str = prev_str + (curr_str * num)

        return curr_str