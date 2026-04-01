class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if digits == "":
            return res
        char_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        def bt(index, curr_str):
            if index == len(digits):
                res.append(curr_str)
                return
            for j in range(len(char_map[digits[index]])):
                bt(index+1, curr_str + char_map[digits[index]][j])
        bt(0, "")
        return res