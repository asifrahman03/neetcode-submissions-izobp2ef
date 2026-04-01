class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        if s == t:
            return s
        
        t_map = {}
        for c in t:
            t_map[c] = 1 + t_map.get(c, 0)

        window_map = {}
        window_match = 0
        need_match = len(t_map)
        l = 0
        res = ""
        resL = len(s)+1
        for r in range(len(s)+1):
            while window_match == need_match:
                windowL = r - l 
                if windowL < resL:
                    resL = windowL
                    res = s[l:r]
                window_map[s[l]] -= 1
                if s[l] in t_map:
                    if t_map[s[l]] - 1 == window_map[s[l]]:
                        window_match -= 1
                if window_map[s[l]] == 0:
                    del window_map[s[l]]
                l += 1
            if r == len(s):
                break
            window_map[s[r]] = 1 + window_map.get(s[r], 0)
            if s[r] in t_map:
                if window_map[s[r]] == t_map[s[r]]:
                    window_match += 1
        return res
