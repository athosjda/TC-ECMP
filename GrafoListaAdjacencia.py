from Grafo import Grafo

class GrafoListaAdjacencia(Grafo):

    def DefinirN(self, n, VizinhancaDuplamenteLigada=False):
        super(GrafoListaAdjacencia, self).DefinirN(n)
        self.L = [None]*(self.n+1)
        for i in range(1,self.n+1):
            self.L[i] = GrafoListaAdjacencia.NoAresta() #nó cabeça 
            self.VizinhancaDuplamenteLigada = VizinhancaDuplamenteLigada
