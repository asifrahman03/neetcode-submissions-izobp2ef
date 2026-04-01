class TimeMap:

    def __init__(self):
        self.pairings = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.pairings[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # Check if key even exists
        if key not in self.pairings:
            return ""

        # LMAO forget use binary search
        res = ""
        l = 0
        r = len(self.pairings[key])-1

        while l <= r:
            mid = (l + r) // 2
            val, prev_time = self.pairings[key][mid]

            if prev_time == timestamp:
                return val
            elif prev_time < timestamp:
                res = val
                l = mid + 1
            else:
                r = mid - 1

        return res
        
