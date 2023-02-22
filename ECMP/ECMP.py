import random as rnd

from GrafoListaAdjacencia import GrafoListaAdjacencia as Grafo

def ECMP(G:Grafo):
    #rnd.seed(1)
    M = inicializacao(G)
    fit = avaliacao(M, G)
    return (M, fit)

def inicializacao(G:Grafo):
    keys = [k for k in G.E()]
    values = [rnd.randint(0, 1) for _ in range(len(keys))]
    return dict(zip(keys, values))

def avaliacao(M, G:Grafo):
    saturado = [0]*(G.n+1)
    fit = 0
    for bit in M:
        if (M[bit] == 1):
            fit = fit+1
            saturado[bit[0]] = saturado[bit[0]]+1
            saturado[bit[1]] = saturado[bit[1]]+1
    
    for idx in saturado:
        print(idx)
        if (idx >= 2):
            fit = fit*(-1)
            break

    return fit