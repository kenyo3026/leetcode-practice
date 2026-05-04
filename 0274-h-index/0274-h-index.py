class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)

        for i, citation in enumerate(citations, 1):

            if i > citation:
                return i - 1

        return i