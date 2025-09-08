class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        cor = [-1] * n  # cores 0 e 1

        for no in range(n):
            if cor[no] != -1: # no ja visitado
                continue

            # DFS no no
            cor[no] = 0
            stack = [no]

            while stack:
                u = stack.pop()
                cor_u = cor[u]
                for v in graph[u]:
                    if cor[v] == -1:
                        cor[v] = cor_u ^ 1  # vizinho ainda n visitado recebe cor oposta
                        stack.append(v)
                    elif cor[v] == cor_u:
                        return False  # mesma cor em camadass diferentes (ciclo impar), n eh bipartido

        return True