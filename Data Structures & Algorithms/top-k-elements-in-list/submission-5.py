class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        freq_list = [[] for _ in range(len(nums) + 1)]

        for i, (key, val) in enumerate(freq.items()):
            freq_list[val].append(key)
        
        count = 0
        res = []
        for i in range(len(freq_list)-1, 0, -1):
            for val in freq_list[i]:
                if count == k:
                    break
                res.append(val)
                count += 1
        return res
