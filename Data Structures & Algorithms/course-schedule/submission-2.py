class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        graph = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses

        for b, a in prerequisites:
            graph[a].append(b)
            indeg[b] += 1
        
        q = deque()
        for course, deg in enumerate(indeg):
            if deg == 0:
                q.append(course)
        
        while q:
            course = q.popleft()

            for pr in graph[course]:
                indeg[pr] -= 1

                if indeg[pr] == 0:
                    q.append(pr)
        for i in range(len(indeg)):
            if indeg[i] != 0:
                return False
        return True