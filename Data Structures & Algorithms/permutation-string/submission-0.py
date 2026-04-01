class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1table = {}
        s2table = {}
        for c in s1:
            if c not in s1table:
                s1table[c] = 1
            else:
                s1table[c] += 1
        
        l = 0
        for r in range(len(s2)):
            c = s2[r]
            if r - l + 1 > len(s1):
                s2table[s2[l]] -= 1
                if s2table[s2[l]] == 0:
                    del s2table[s2[l]]
                l += 1
            if c not in s2table:
                s2table[c] = 1
            else:
                s2table[c] += 1
            if r - l + 1 == len(s1):
                if s1table == s2table:
                    return True
        return False