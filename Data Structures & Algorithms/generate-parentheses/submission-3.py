class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        open_p = n
        closed_p = n

        def bt(curr_s, o_p, c_p):
            if o_p == 0 and c_p == 0:
                res.append(curr_s)
                return
            if o_p > 0:
                bt(curr_s + '(', o_p-1, c_p)
            if c_p > o_p:
                bt(curr_s + ')', o_p, c_p-1)
            return
        bt("", open_p, closed_p)
        return res
                