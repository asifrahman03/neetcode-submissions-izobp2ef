class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for source, dest in sorted(tickets)[::-1]:
            adj[source].append(dest)
        
        res = []
        def dfs(airport):
            while adj[airport]:
                dest = adj[airport].pop()
                dfs(dest)
            res.append(airport)
        
        dfs("JFK")
        return res[::-1]
