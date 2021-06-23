from Grafo import Grafo
import scipy.special as spy

import numpy as np

class ECMP:
    def __init__(self, G:Grafo):
        self.G = G
        self.a = np.random.randint(2, size=G.m)
        self.d = np.zeros(G.n)
        self.b = [(1/G.m)*i for i in range(G.m + 1)]
        self.s = sum(self.a)
        
        self._ultimo_bit = -1

    def ea_1p1(self):
        s = 0
        c = 0
        
        for idx, edge in enumerate(self.G.edges):
            s += self.a[idx]
            self.d[edge[0]] += 1
            self.d[edge[1]] += 1
        
        for ele in self.d:
            c += spy(ele, 2)

        return c > 0 and -c or s
