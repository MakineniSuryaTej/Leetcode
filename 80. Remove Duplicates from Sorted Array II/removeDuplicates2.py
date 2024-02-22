class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = dict()
        ind = 0
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
                if d[nums[i]] <= 2:
                    nums[ind] = nums[i]
                    ind += 1
            else:
                d[nums[i]] = 1
                nums[ind] = nums[i]
                ind += 1
        return ind
