from Grafo import Grafo

class GrafoListaAdjacencia(Grafo):

    class No(object):
        def __inti__(self):
            self.vizinho = None
            self.e = None
            self.proximo = None
    
    class Aresta(object):
        def __init__(self):
            self.v1, self.no1 = None, None
            self.v2, self.no2 = None, None

    def definir_n(self, n, VizinhancaDuplamenteLigada=False):
        super(GrafoListaAdjacencia, self).definir_n(n)
        self.L = [None]*(self.n+1)
        for i in range(1,self.n+1):
            self.L[i] = GrafoListaAdjacencia.No
            self.VizinhancaDuplamenteLigada = VizinhancaDuplamenteLigada

    def adicionar_aresta(self, u, v):
        def adicionar_lista(u, v, e, tipo):
            no = GrafoListaAdjacencia.No()
            no.vizinho = v
            no.e = e
            no.proximo = self.L[u].proximo
            self.L[u].proximo = no
            if (self.L[u].proximo.proximo != None):
                self.L[u].proximo.proximo.anterior = self.L[u].proximo
            if self.orientado:
                no.tipo = tipo
        
        e = GrafoListaAdjacencia.Aresta()
        e.v1 = u
        e.v2 = v
        e.no1 = adicionar_lista(u, v, e, "+")
        e.no2 = adicionar_lista(u, v, e, "-")

        self.m = self.m+1
        
        return e