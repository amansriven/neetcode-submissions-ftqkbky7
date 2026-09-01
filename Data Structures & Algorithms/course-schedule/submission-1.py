class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        graph = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses

        for b, a in prerequisites:
            indeg[b] += 1
            graph[a].append(b)

        q = deque()
        for i in range(len(indeg)):
            if indeg[i] == 0:
                q.append(i)

        while q:
            course = q.popleft()

            for nextclass in graph[course]:
                indeg[nextclass] -= 1
                if indeg[nextclass] == 0:
                    q.append(nextclass)
        
        for i in range(len(indeg)):
            if indeg[i] != 0:
                return False
    
        return True

