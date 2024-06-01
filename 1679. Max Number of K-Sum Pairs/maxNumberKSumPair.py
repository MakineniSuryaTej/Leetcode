class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        operations, i, j = 0, 0, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] == k:
                operations += 1
                i += 1
                j -= 1
            elif nums[i] + nums[j] < k:
                i += 1
            else:
                j -= 1
        return operations
