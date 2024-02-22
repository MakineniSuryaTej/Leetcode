class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set()
        ind = 0
        for i in range(len(nums)):
            if nums[i] not in s:
                nums[ind] = nums[i]
                s.add(nums[i])
                ind += 1
        return ind
