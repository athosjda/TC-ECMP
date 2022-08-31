from operator import index
from Grafo import Grafo

class Emparelhamento:
    def __init__(self, G:Grafo):
        
        self._G = G
        self._M = [None]*(G.n+1)

    def emperelhamento(self):
        
        while True:
            p = self.caminho_aumentante()
            if len(p) == 0:
                return self._M    
            
    def caminho_aumentante(self):
        F = []
        E = []
        P = []
        raiz = [-1]*self._G.n
        distancia = [-1]*self._G.n
        for v in self._G.vertex:
            if v not in self._M:
                F.append({v, []})
                raiz[v] = v
                distancia[v] = 0
        for e in self._G.edges:
            E.append(e)
        for e in self._M:
            if e in self._M:
                E.remove(e)
        for v in F:
            for e in E:
                if e['w'] not in F:
                    # adicionar na floresta
                    pass
                else:
                    if distancia[e['w']]%2 == 0:
                        if raiz[e['v']] != raiz[e['w']]:
                            # retorna o caminho aumentante
                            pass
                        else:
                            # resolve o "broto" haha
                            pass
                        return P
                E.remove(e)
        return P

    def adiciona_na_floresta(self, F, v, w, raiz):
        x = self._M[w]
        F[v].append(w)
        F.append((w, []))
        F[w].add(x)
        raiz[w] = raiz[v]
        raiz[x] = raiz[v]

    def contrai_blossom(self, B, w):
        for v in self._G.vertex:
            for u in self._G.adj[v]:
                if u in B:
                    u = w
                if v in B:
                    v = w
                if v != u and u not in self._G.adj[v]:
                    self._G.adj[v].append(u)
