class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l, r = 0, 0
        replacements = 0
        char_map = {}
        while r < len(s):
            if s[r] not in char_map:
                char_map[s[r]] = 1
            else:
                char_map[s[r]] += 1
            for v in char_map.values():
                replacements = max(replacements, v)
            while (r -l + 1) - replacements > k:
                char_map[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res