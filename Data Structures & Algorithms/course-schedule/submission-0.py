class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_map = defaultdict(list)

        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)

        visited = set()
        safe = set()
        def dfs(course):
            if course in visited:
                return False
            if course in safe:
                return True
            visited.add(course)
            for prereq in prereq_map[course]:
                if dfs(prereq) == False:
                    return False
            visited.remove(course)
            safe.add(course)
            return True
            
        
        for course in range(numCourses):
            if dfs(course) == False:
                return False
        return True
            