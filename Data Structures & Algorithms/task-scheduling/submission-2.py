class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        pairs = []
        for letter, val in count.items():
            pairs.append((-val, letter))
        heapq.heapify(pairs)

        cooldown = deque()
        time = 0
        while cooldown or pairs:
            time += 1
            if pairs:
                freq, task = heapq.heappop(pairs)
                freq += 1
                if freq != 0:
                    cooldown.append((task, time + n, freq))
            if cooldown and cooldown[0][1] == time:
                task, _, freq = cooldown.popleft()
                heapq.heappush(pairs, (freq, task))
        return time

