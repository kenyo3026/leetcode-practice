class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        left, right = 0, 0
        count_hash = {"a":0, "b":0, "c":0}
        n_of_substrings = 0

        while right < n:
            count_hash[s[right]] += 1

            # while all(count_hash.values()):
            while count_hash["a"] > 0 and count_hash["b"] > 0 and count_hash["c"] > 0:
                n_of_substrings += n - right
                count_hash[s[left]] -= 1
                left += 1

            right += 1

        return n_of_substrings