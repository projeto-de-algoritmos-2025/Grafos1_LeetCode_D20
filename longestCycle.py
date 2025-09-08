class Solution(object):
    def longestCycle(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        n = len(edges)
        visited = [False] * n
        ans = -1

        for i in range(n):
            if visited[i]:
                continue

            atual = i
            step = 0 # numero de passos na rodada
            pos_local = {}  # ordem de visita da rodada

            while atual != -1 and not visited[atual] and atual not in pos_local:
                pos_local[atual] = step
                step += 1
                atual = edges[atual]

            # Se o while parou por um no ja visitado na rodada eh pq tem ciclo
            if atual in pos_local:
                ans = max(ans, step - pos_local[atual])

            for node in pos_local:
                visited[node] = True

        return ans