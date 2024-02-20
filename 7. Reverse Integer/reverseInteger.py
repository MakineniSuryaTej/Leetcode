class Solution:
    def reverse(self, x: int) -> int:
        prevNum, revNum, temp = 0, 0, abs(x)
        while(temp != 0):
            r = temp % 10
            revNum = revNum * 10 + r
            if revNum not in range(-2**31, 2**31):
                revNum = 0
            if (revNum - r)//10 != prevNum:
                return 0
            prevNum = revNum
            temp = temp // 10
        if x < 0:
            return -revNum
        else:
            return revNum
        
