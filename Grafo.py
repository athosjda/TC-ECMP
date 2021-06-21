class Grafo:
    def __init__(self, n, direcionado=False):
        self.n = n
        self.m = 0
        self.edges = []
        self.adj = [[] for _ in range(n)]

        self._direcionado = direcionado

    def inserir_arestas(self, u, v):
        self.adj[u].append(v)
        self.edges.append((u, v))
        if not self._direcionado:
            self.adj[v].append(u)
        self.m += 1
