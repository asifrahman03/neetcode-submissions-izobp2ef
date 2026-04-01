class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        rules = defaultdict(set)
        indegree = {c: 0 for w in words for c in w}

        for l in range(len(words) - 1):
            w1, w2 = words[l], words[l + 1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for i in range(min_len):
                if w1[i] != w2[i]:
                    if w2[i] not in rules[w1[i]]:
                        rules[w1[i]].add(w2[i])
                        indegree[w2[i]] += 1
                    break

        q = deque([c for c in indegree if indegree[c] == 0])

        res = ""
        while q:
            curr_c = q.popleft()
            res += curr_c

            if curr_c in rules:
                for nei_c in rules[curr_c]:
                    indegree[nei_c] -= 1
                    if indegree[nei_c] == 0:
                        q.append(nei_c)

        return res if len(res) == len(indegree) else ""