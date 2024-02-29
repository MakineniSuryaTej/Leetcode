class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1, d2 = dict(), dict()
        for i in ransomNote:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        for i in magazine:
            if i in d2:
                d2[i] += 1
            else:
                d2[i] = 1
        
        for i in d1.keys():
            count = d2.get(i, "null")
            if count == "null" or count < d1[i]:
                return False
        return True
