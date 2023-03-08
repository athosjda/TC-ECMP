import random as rnd
import math 

from GrafoListaAdjacencia import GrafoListaAdjacencia as Grafo

def ECMP(G:Grafo, x):
    rnd.seed(1)
    M = inicializacao(G)
    b = probabilidade(len(M))
    fit = avaliacao(M, G)
    while x:
        Ml = mutacao(M, abs(1/fit), b)
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
    
    c = 0
    for idx in saturado:
        if (idx >= 2):
            c = c+1

    return fit if (c == 0) else c*(-1)

def mutacao(M, p, b):
    r = rnd.random()
    t = linear_search(b, r)
    Ml = M.copy()
    bit_m = set()
    bit = 0
    bits = list(M.keys())
    while t:
        while True:
            bit = rnd.randint(0, len(M)-1)
            if (bit not in bit_m):
                bit_m.add(bit)
                break
        Ml[bits[bit]] = not Ml[bits[bit]]
        t = t-1
        
    ''' Conferir na bibliografia :v
    for bit in M:
        pl = rnd.random()
        if (pl < p):
            Ml[bit] = not Ml[bit]
    '''
    return Ml

def probabilidade(m):
    b = [0]*(m+1)
    b[0] = 0
    for i in range(0, m):
        b[i+1] = (math.comb(m, i)*((1/m)**i)*((1-(1/m))**(m-i)))+b[i]
    b[-1] = 1
    return b

def linear_search(b, r):
    j = 1
    for i in range(len(b)):
        if (b[i] <= r) and (r < b[i+1]):
            j = i+1
    return j