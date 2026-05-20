class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        A_set, B_set = set(), set()
        C = []
        n = len(A)

        for i in range(n):
            A_set.add(A[i])
            B_set.add(B[i])

            same = len(A_set & B_set)
            C.append(same)

        return C