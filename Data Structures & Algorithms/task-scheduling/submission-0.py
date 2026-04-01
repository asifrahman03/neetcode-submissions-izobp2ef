class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        heap = []
        for i, cnt in enumerate(freq):
            if cnt > 0:
                heap.append((-cnt, chr(i + ord('A'))))
        heapq.heapify(heap)

        time = 0
        cooldown = deque()  # left = newest, right = next ready

        while heap or cooldown:
            time += 1

            if heap:
                cnt, task = heapq.heappop(heap)
                cnt += 1
                if cnt < 0:
                    cooldown.appendleft((time + n, cnt, task))

            while cooldown and cooldown[-1][0] <= time:
                _, cnt, task = cooldown.pop()
                heapq.heappush(heap, (cnt, task))

        return time
