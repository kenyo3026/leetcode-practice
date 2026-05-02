class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash = {}

        for num in arr:
            if not num in hash:
                hash[num] = 1
            else:
                hash[num] += 1

        return len(set(hash.values())) == len(hash.values())