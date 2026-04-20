class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        queue_radiant = deque([])
        queue_dire = deque([])

        for i in range(n):
            if senate[i] == "R":
                queue_radiant.append(i)
            else:
                queue_dire.append(i)

        while queue_radiant and queue_dire:
            turn_radiant = queue_radiant.popleft()
            turn_dire = queue_dire.popleft()

            if turn_radiant < turn_dire:
                queue_radiant.append(turn_radiant + n)
            else:
                queue_dire.append(turn_dire + n)

        return "Radiant" if queue_radiant else "Dire"