class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}

        for word in strs:
            pattern = tuple(sorted(word))

            if not pattern in hash:
                hash[pattern] = [word]
            else:
                hash[pattern].append(word)

        return list(hash.values())