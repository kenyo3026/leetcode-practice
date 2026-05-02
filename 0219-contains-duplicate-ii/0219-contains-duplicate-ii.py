class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash = {}
        n = len(nums)

        for i in range(n):

            if not nums[i] in hash:
                hash[nums[i]] = [i]
                continue

            for j in hash[nums[i]]:
                if abs(i - j) <= k:
                    return True

            hash[nums[i]].append(i)

        return False