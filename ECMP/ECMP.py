import random as rnd

from GrafoListaAdjacencia import GrafoListaAdjacencia as Grafo

def ECMP(G:Grafo, x):
    rnd.seed(1)
    M = inicializacao(G)
    fit = avaliacao(M, G)
    while x:
        Ml = mutacao(M, abs(1/fit))
        fitl =avaliacao(Ml, G)
        if (fitl > fit):
            M = Ml.copy()
            fit = fitl
        x = x-1
    return (M, fit)

def inicializacao(G:Grafo):
    keys = [k for k in G.E()]
    values = [(True if rnd.randint(0, 1) else False) for _ in range(len(keys))]
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
        if (idx >= 2):
            fit = fit*(-1)
            break

    return fit

def mutacao(M, p):
    Ml = M.copy()
    for bit in M:
        pl = rnd.random()
        if (pl < p):
            Ml[bit] = not Ml[bit]
    return Ml