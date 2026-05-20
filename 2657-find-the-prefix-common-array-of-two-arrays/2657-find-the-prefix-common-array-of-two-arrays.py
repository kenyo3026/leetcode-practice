class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        A_set, B_set = set(), set()
        C = []
        n = len(A_set)

        for i, (a, b) in enumerate(zip(A, B), 1):
            A_set.add(a)
            B_set.add(b)

            same = i - len(A_set - B_set)
            C.append(same)

        return C