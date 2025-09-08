class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        if source == destination:
            return True

        # lista de adjacencia
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # DFS pra procurar destination na lista de adjacencia a partir de source
        visited = [False] * n
        stack = [source]
        visited[source] = True

        while stack:
            u = stack.pop()
            if u == destination:
                return True
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)

        return False