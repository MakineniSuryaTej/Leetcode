class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = ''.join([i for i in s if ord(i) in range(97, 123) or ord(i) in range(65, 91) or ord(i) in range(48, 58)]).lower()
        # return s == s[::-1]
        temp = ""
        for i in s:
            if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z') or (i >= '0' and i <= '9'):
                temp += i
        temp = temp.lower()
        i, j = 0, len(temp) - 1
        while i <= j:
            if temp[i] != temp[j]:
                return False
            i += 1
            j -= 1
        return True 
