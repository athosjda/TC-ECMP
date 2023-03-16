import time
from GrafoListaAdjacencia import GrafoListaAdjacencia
from Edmonds.emparelhamento import emparelhamento_geral
from ECMP.ecmp import ECMP

def TamEmpa(m):
    t = 0
    for v in m:
        if v != None:
            t = t + 1
    return t/2

if __name__ == '__main__':
    g : GrafoListaAdjacencia = GrafoListaAdjacencia()
    
    n, m = input().split()
    n, m = int(n), int(m)
    g.definir_n(n)
    for _ in range(m):
        v, u = input().split()
        v, u = int(v), int(u)
        g.adicionar_aresta(v, u)

    #m = emparelhamento_geral(g)
    #print(TamEmpa(m))
    inicio = time.time()
    m = ECMP(g)
    fim = time.time()
    print(m[1])
    print(f"{fim-inicio} segundos")
    