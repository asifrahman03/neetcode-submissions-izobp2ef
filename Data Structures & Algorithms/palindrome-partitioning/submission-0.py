class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res= []

        def bt(index, curr_set):
            if index == len(s):
                res.append(curr_set[:])
                return
            for i in range(index, len(s)):
                # if i > index and s[i-1] == s[i]:
                #     continue
                l = index
                r = i
                is_p = True
                while l <= r:
                    if s[l] != s[r]:
                        is_p = False
                        break
                    l += 1
                    r -= 1
                if is_p:
                    curr_set.append(s[index:i+1])
                    bt(i+1, curr_set)
                    curr_set.pop()

        bt(0, [])
        return res