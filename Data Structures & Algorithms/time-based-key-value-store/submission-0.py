class TimeMap:

    def __init__(self):
        self.pairings = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.pairings[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # Check if key even exists
        if key not in self.pairings:
            return ""

        res = ""
        for i in range(len(self.pairings[key])):
            val, prev_time = self.pairings[key][i]
            if prev_time <= timestamp:
                res = val

        return res
        
