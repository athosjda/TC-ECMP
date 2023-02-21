from Grafo import Grafo

class GrafoListaAdjacencia(Grafo):

    class No(object):
        def __init__(self):
            self.vizinho = None
            self.e = None
            self.proximo = None
            self.tipo = None
    
    class Aresta(object):
        def __init__(self):
            self.v1 = None
            self.no1 = None
            self.v2 = None
            self.no2 = None

    def definir_n(self, n, VizinhancaDuplamenteLigada=False):
        super(GrafoListaAdjacencia, self).definir_n(n)
        self.L = [None]*(self.n+1)
        for i in range(1,self.n+1):
            self.L[i] = GrafoListaAdjacencia.No()
            self.VizinhancaDuplamenteLigada = VizinhancaDuplamenteLigada

    def adicionar_aresta(self, u, v):
        def adicionar_lista(u, v, e, tipo):
            no = GrafoListaAdjacencia.No()
            no.vizinho = v
            no.e = e
            no.proximo = self.L[u].proximo
            self.L[u].proximo = no
            if self.VizinhancaDuplamenteLigada:
                self.L[u].Prox.Ant = self.L[u]
            if (self.L[u].proximo.proximo != None):
                self.L[u].proximo.proximo.anterior = self.L[u].proximo
            if self.orientado:
                no.tipo = tipo
            return no
        
        e = GrafoListaAdjacencia.Aresta()
        e.v1 = u
        e.v2 = v
        e.no1 = adicionar_lista(u, v, e, '+')
        e.no2 = adicionar_lista(v, u, e, '-')

        self.m = self.m+1

        return e
    
    def remover_aresta(self, uv):
        def remover_lista(no):
            no.anterior.proximo = no.proximo
            if (no.proximo != None):
                no.proximo.anterior = no.anterior
        remover_lista(uv.no1)
        remover_lista(uv.no2)
    
    def sao_adjacentes(self, u, v):
        tipo = '+' if self.orientado else '*'

        for w in self.N(u, tipo):
            if (w == v):
                return True
        return False

    def N(self, v, tipo='*', fechada=False, iterar_sobre_no=False):
        if fechada:
            no = GrafoListaAdjacencia.No()
            no.vizinho = v
            no.e = None
            no.proximo = None
        w = self.L[v].proximo
        while (w != None):
            if (tipo == '*') or (w.tipo == tipo):
                yield w if iterar_sobre_no else w.vizinho
            w = w.proximo
