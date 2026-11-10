class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        far_count = 0

        for a1 in arr1:
            flag = True
            for a2 in arr2:
                if abs(a1 - a2) <= d:
                    flag = False
                    break

            if flag:
                far_count += 1

        return far_count