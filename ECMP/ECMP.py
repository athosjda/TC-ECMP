from Grafo import Grafo
import numpy as np

class ECMP:
    def __init__(self, G:Grafo):
        self.a = np.random.randint(2, size=G.m)

    def fitness(self):
        return sum(self.a)