class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word))
            res += "#"
            res += word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        l = 0
        r = 0
        while r < len(s):
            if s[r] == '#':
                wordLS = s[l:r]
                wordL = int(wordLS)
                word = s[(r+1) : (r + wordL + 1)]
                res.append(word)
                l = r + wordL + 1 
                r = l
            r+=1
        return res

