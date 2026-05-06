class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        n, m = len(boxGrid), len(boxGrid[0])

        # stage 1: move stones to the right
        for row in range(n):
            empty = m - 1

            for j in range(m-1, -1, -1):
                if boxGrid[row][j] == '.':
                    continue
                elif boxGrid[row][j] == '#':
                    if j != empty:
                        boxGrid[row][empty] = '#'
                        boxGrid[row][j] = '.'
                    empty -= 1
                elif boxGrid[row][j] == '*':
                    empty = j - 1

        # stage 2: rotate 90 degrees clockwise
        return list(zip(*boxGrid[::-1]))
