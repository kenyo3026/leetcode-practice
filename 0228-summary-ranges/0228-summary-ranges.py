class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        n = len(nums)
        summarized = [[nums[0]]]

        for i in range(1, n):

            if nums[i] - summarized[-1][-1] == 1:
                summarized[-1].append(nums[i])

            else:
                if len(summarized[-1]) > 1:
                    summarized[-1] = f"{summarized[-1][0]}->{summarized[-1][-1]}"
                else:
                    summarized[-1] = str(summarized[-1][0])

                summarized.append([nums[i]])

        if len(summarized[-1]) > 1:
            summarized[-1] = f"{summarized[-1][0]}->{summarized[-1][-1]}"
        else:
            summarized[-1] = str(summarized[-1][0])

        return summarized