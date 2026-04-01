class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_map = defaultdict(list)

        for course, pre in prerequisites:
            prereq_map[course].append(pre)
        
        visited = set()
        safe = set()
        output = []
        def dfs(course):
            if course in visited:
                return False
            if course in safe:
                return True
            visited.add(course)
            for pre in prereq_map[course]:
                if dfs(pre) == False:
                    return False
            visited.remove(course)
            safe.add(course)
            output.append(course)
            return True
        

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output
