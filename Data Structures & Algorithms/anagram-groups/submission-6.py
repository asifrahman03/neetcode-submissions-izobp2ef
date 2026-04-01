from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for string in strs:
            arr = [0] * 26
            for c in string:
                arr[ord(c)-ord('a')] += 1
            key_s = tuple(arr)
            res[key_s].append(string)
        return list(res.values()) 

