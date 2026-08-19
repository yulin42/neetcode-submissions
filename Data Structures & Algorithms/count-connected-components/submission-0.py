class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for i in range(n)]
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        visiting = set()

        def dfs(node):
            if node in visiting:
                return

            visiting.add(node)
            for nei in graph[node]:
                dfs(nei)
        
        res = 0
        for node in range(n):
            if node not in visiting:
                dfs(node)
                res += 1
        
        return res