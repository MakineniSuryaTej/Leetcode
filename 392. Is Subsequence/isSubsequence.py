class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m, count = len(s), len(t), 0
        for i in range(m):
            if count < n and s[count] == t[i]:
                count += 1
        return count == n
        
