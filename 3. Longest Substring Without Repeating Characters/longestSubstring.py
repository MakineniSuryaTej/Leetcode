class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cl = [0]
        d = dict()
        i,c = 0,0
        #s = s.replace(' ','_')
        while i < len(s):
            if s[i] in d:
                i = d[s[i]] + 1
                cl.append(c)
                c=0
                d.clear()
            else:
                d[s[i]] = i
                c += 1
                i += 1
        cl.append(c)
        return max(cl)
