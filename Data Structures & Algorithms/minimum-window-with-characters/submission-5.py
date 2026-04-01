class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        
        curr, countT = {}, {}

        for c in t:
            countT[c] = 1+countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            char = s[r];
            curr[char] = 1 + curr.get(char, 0)

            if char in countT and curr[char] == countT[char]:
                have+=1
            
            while have == need:
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = r-l+1
                curr[s[l]] -= 1
                if s[l] in countT and curr[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""