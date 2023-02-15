class Grafo(object):
    def __init__(self, orientado=False):
        self.n = None
        self.m = None
        self.orientado = orientado

    def definir_n(self, n):
        self.n = n
        self.m = 0
    
    def V(self):
        for i in range(1, self.n+1):
            yield i

    def E(self, iterar_sobre_no=False):
        for v in self.V():
            for w in self.N(v, tipo = '+' if self.orientado else '*', iterar_sobre_no = iterar_sobre_no):
                enumerar = True
                if not self.orientado:
                    wint = w if isinstance(w, int) else w.viz
                enumerar = v < wint
        if enumerar:
            yield (v, w)