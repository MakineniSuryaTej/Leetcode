class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict(zip(nums, list(range(len(nums)))))
        for i in range(len(nums)):
            value = d.get(target-nums[i],-1)
            if value != -1 and value != i:
                return [i,value]
