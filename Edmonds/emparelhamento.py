from Grafo import Grafo

class Emparelhamento:
    def __init__(self, G:Grafo):
        self._G = G
        self._M = []
        self._P = []

    def emperelhamento(self):
        self.M = [None]*(G.n+1)
        
        while True:
            self._P = reducao_flor()
            self._M = diferenca_simentrica()
            if len(self._P) == 0:
                break
            return self._M

    def reducao_flor():
        return []

    def diferenca_simetrica():
        return []