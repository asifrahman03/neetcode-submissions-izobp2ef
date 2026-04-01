class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        l,r = 0,0
        res = 0
        while r < len(s):
            while s[r] in visited:
                visited.remove(s[l])
                l += 1
            res = max(res, r-l+1)
            visited.add(s[r])
            r += 1
        return res