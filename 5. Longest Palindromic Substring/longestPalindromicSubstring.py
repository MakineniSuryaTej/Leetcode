class Solution:
    def helper(self,s: str, i: int, j: int) -> str:
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i + 1:j]
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        maxS = s[0]
        for _ in range(len(s) - 1):
            str1 = self.helper(s, _, _ + 1)
            str2 = self.helper(s, _, _)
            if len(maxS) < len(str1):
                maxS = str1 
            if len(maxS) < len(str2):
                maxS = str2 
        return maxS
            
