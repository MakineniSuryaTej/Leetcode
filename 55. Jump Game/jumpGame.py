class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = 0
        for i in nums:
            if jump < 0:
                return False
            if jump < i:
                jump = i
            jump -= 1
        return True
