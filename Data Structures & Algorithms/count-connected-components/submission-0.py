class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for ne in adj[node]:
                dfs(ne)

        res = 0
        for node in range(n):
            if node not in visited:
                res += 1
                dfs(node)
        return res