class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        res = 0
        cset = set()
        while r < len(s):
            while s[r] in cset:
                cset.remove(s[l])
                l+=1
            cset.add(s[r])
            r += 1 
            res = max(r - l, res)
        return res