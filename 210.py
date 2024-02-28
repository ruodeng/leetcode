from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        prerequisites.sort(key=lambda x: x[1]) # sort by
        print(prerequisites)
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for i in range(len(prerequisites)):
            graph[prerequisites[i][1]].append(prerequisites[i][0])

        visited = [0] * numCourses
        result = []
        def dfs(node):
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True
            visited[node] = 1
            for i in graph[node]:
                if not dfs(i):
                    return False
            visited[node] = 2
            result.append(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        result.reverse()
        return result




# x,0,1,2,3
# 0,x,1,1,0
# 1,x,x,0,1
# 2,x,x,0,1

s = Solution()
print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
print(s.findOrder(2, [[1,0]]))
print(s.findOrder(1, [ ]))
