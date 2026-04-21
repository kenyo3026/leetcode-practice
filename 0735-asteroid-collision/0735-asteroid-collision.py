class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:

            while stack and asteroid != None and \
                (stack[-1] > 0) and (asteroid < 0):
                    a = abs(stack[-1])
                    b = abs(asteroid)

                    if a == b:
                        stack.pop()
                        asteroid = None
                    elif a > b:
                        asteroid = None
                    elif a < b:
                        stack.pop()

            if asteroid:
                stack.append(asteroid)
        return stack

            