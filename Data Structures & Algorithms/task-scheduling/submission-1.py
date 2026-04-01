class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        # 1. Build frequency map
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        # 2. Max heap of (-count, task)
        heap = []
        for i, cnt in enumerate(freq):
            if cnt > 0:
                heap.append((-cnt, chr(i + ord('A'))))
        heapq.heapify(heap)

        time = 0
        cooldown = deque()  # (ready_time, -count, task)

        # 3. Simulation
        while heap or cooldown:
            time += 1

            # Execute a task if possible
            if heap:
                cnt, task = heapq.heappop(heap)
                cnt += 1  # one instance used

                if cnt < 0:
                    cooldown.append((time + n, cnt, task))

            # Release tasks whose cooldown expired
            if cooldown and cooldown[0][0] == time:
                _, cnt, task = cooldown.popleft()
                heapq.heappush(heap, (cnt, task))

        return time
