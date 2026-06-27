class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        num_tags = [1 if num == target else -1 for num in nums]
        # prefix_sums = [0]
        # for i in range(n):
        #     prefix_sums.append(prefix_sums[-1] + num_tags[i])

        subarray_counts = 0
        for i in range(n):
            prefix_sum_so_far = 0
            for j in range(i, n):
                prefix_sum_so_far += num_tags[j]
                if prefix_sum_so_far > 0:
                    subarray_counts += 1

        return subarray_counts