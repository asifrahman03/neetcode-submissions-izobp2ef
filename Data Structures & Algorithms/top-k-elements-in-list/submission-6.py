class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        arr = [[] for _ in range(len(nums)+1)]
        for n in freq.keys():
            arr[freq[n]].append(n)
        
        res = []
        for i in range(len(arr)-1, -1, -1):
            if arr[i]:
                for j in range(len(arr[i])-1, -1, -1):
                    if k > 0:
                        res.append(arr[i][j])
                        k-=1
        return res

