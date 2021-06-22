from Grafo import Grafo
from Funcoes import *

import numpy as np

class ECMP:
    def __init__(self, G:Grafo):
        self.G = G
        self.a = np.random.randint(2, size=G.m)
        self.d = np.zeros(G.n)

    def ea_1p1(self):
        s = 0
        c = 0
        
        for idx, edge in enumerate(self.G.edges):
            s += self.a[idx]
            self.d[edge[0]] += 1
            self.d[edge[1]] += 1
        
        for ele in self.d:
            c += binomio_newton(ele, 2)

        return c > 0 and -c or s
