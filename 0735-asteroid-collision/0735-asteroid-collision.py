class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:

            while stack and asteroid != None and \
                asteroid < 0 < stack[-1]:

                if stack[-1] == -asteroid:
                    stack.pop()
                    asteroid = None
                elif stack[-1] > -asteroid:
                    asteroid = None
                elif stack[-1] < -asteroid:
                    stack.pop()

            if asteroid:
                stack.append(asteroid)
        return stack

            