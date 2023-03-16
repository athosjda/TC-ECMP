import random as rnd

from GrafoListaAdjacencia import GrafoListaAdjacencia as Grafo

def ECMP(G:Grafo):
    t = 0
    M = inicializacao(G)
    fit = avaliacao(M, G)
    while t < (G.n*20):
        Ml = mutacao(M, 1.0/(len(M)))
        fitl =avaliacao(Ml, G)
        if (fitl > fit):
            M = Ml.copy()
            fit = fitl
        t = t+1
        print(fit)
    return (M, fit)


def inicializacao(G:Grafo):
    keys = [k for k in G.E()]
    saturados = [True]*(G.n+1)
    values = []
    for e in keys:
        if rnd.randint(0, 1) and saturados[e[0]] and saturados[e[1]]:
            values.append(True)
        else: 
            values.append(False)
        saturados[e[0]] = False
        saturados[e[1]] = False 
    return dict(zip(keys, values))

def avaliacao(M, G:Grafo):
    saturado = [0]*(G.n+1)
    fit = 0
    for bit in M:
        if (M[bit] == 1):
            fit = fit+1
            saturado[bit[0]] = saturado[bit[0]]+1
            saturado[bit[1]] = saturado[bit[1]]+1
    
    c = 0
    for idx in saturado:
        if (idx >= 2):
            c = c+1

    return fit if (c == 0) else c*(-1)

def mutacao(M, p):
    Ml = M.copy()
    numM = 0
    bits = list(M.keys())
    for bit in Ml:
        r = rnd.random()
        if r < p:
            Ml[bit] = not Ml[bit]
            numM = numM + 1
    if numM == 0:
        numM = numM + 1
        bit = bits[rnd.randint(0, len(bits)-1)]
        Ml[bit] = not Ml[bit]
    return Ml
