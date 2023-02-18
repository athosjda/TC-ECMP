from GrafoListaAdjacencia import GrafoListaAdjacencia as Grafo

def emparelhamento_geral(G:Grafo):
    M = [None]*(G.n+1)
    while True:
        P = reducao_blossom(G, M)
        M = diferenca_simetrica(M, P) # conferir a implementação da diferença simétrica
        if len(P) == 0:
            break
    return M

def reducao_blossom(G:Grafo, M):
    (P, F, H) = aumentante(G, M)
    if len(P) > 0 and F != None:
        (GF, MF) = obter_GFMF(G, M, F, H)
        Plin = reducao_blossom(GF, MF)
        P = contrucao_1(G, GF, F, H, M, Plin)
    return P

def aumentante(G:Grafo, M):
    Df = Grafo()
    Df.definir_n(G.n)
    Df.expressao_associada = [None]*(Df.n+1)
    for v in G.V():
        for w in G.N(v):
            if M[w] != v:
                if M[w] == None:
                    Df.expressao_associada[v] = w
                else:
                    e =  Df.adicionar_aresta(v, M[w])
                    e.inter = w  # Conferir na bibliografia a estrutura de grafos como é definido um Nó
    
    Df.Exp = [True]*(Df.n+1)
    for v in M:
        if v != None:
            Df.expressao_associada[v] = False
    Pf = BuscaCaminhoAumentante(Df)
    (P, F, H) = construcao_3(Pf, Df, G, M)

    return (P, F, H)

def obter_GFMF(G:Grafo, M, F, H):
    GF:Grafo = Grafo(orientado=False)
    GF.definir_n(G.n-len(F)+1)
    GF.VAssocD = [None]*(GF.n+1)
    G.VAssocO = [None]*(GF.n+1)
    G.VizEmF = [None]*(GF.n+1)

    aresta_com_flor = [False]*(G.n+1)

    for v in F:
        G.VAssocO[v] = 1
    GF.VAssocD[1] = F[0]

    n = 2

    for v in G.V():
        if (G.VAssocO[v] == None):
            G.VAssocO[v] = n
            GF.VAssocO[n] = v
            n = n+1
    
    MF = [None]*(GF.n+1)

    for v in G.V():
        if (M[v] != None) and (G.VAssocO[v] != G.VAssocO[M[v]]):
            MF[G.VAssocO[v]] = G.VAssocO[M[v]]
    
    for v in G.V():
        for w in G.N(v):
            if (v < w):
                (x, y) = (v, w) if G.VAssocO[v] == 1 else (w, v)
                if (G.VAssocO[y] != 1):
                    if (G.VAssocO[x] == 1):
                        if (G.VizEmF[y] == None) or (GF.VAssocD[1] == x):
                            G.VizEmF[y] = x
                        if not aresta_com_flor[y]:
                            aresta_com_flor[y] = True
                            GF.adicionar_aresta(G.VAssocO[x], G.VAssocO[y])
                        else:
                            GF.adicionar_aresta(G.VAssocO[x], G.VAssocO[y])
    
    return (GF, MF)



def construcao_3(Pf, Df, G, M):
    Ciclo = None 
    H = None
    
    VMarcado = [-1]*(Df.n+1)
    i = 0
    for v in Pf:
        if VMarcado[v] > -1:
            ciclo = Pf[VMarcado[v]:i]
            H = Pf[:VMarcado[v]+1]
            break
        else:
            VMarcado[v] = i
            i = i+1
    return (Pf, Ciclo, H)

def busca_caminho_aumentante(D:Grafo):

    def P(v):
        D.marcado[v] = True
        Q = [v]
        if D.expressao_associada[v] != None and (not D.marcado[D.expressao_associada[v]]):
            Q.append(D.expressao_associada[v])
            return True
        for w_no in D.N(v, "+", IterarSobreNo=True): # Revisa estrutura da classe de Grafos
            w = w_no.Viz
            if not D.marcado[w] and (not D.marcado[w_no.e.inter] or not w_no.e.inter in Q):
                Q.append(w_no.e.inter)
            if P(w):
                return True
            Q.pop()
        Q.pop()
        return False 

    Q = []
    for s in D.v():
        if D.expressao[s]:
            D.marcado = [False]*(D.n+1)
            if P(s):
                break
    return Q

def diferenca_simetrica(M, P):
    MR  = [v for v in M]
    for i in range(0, len(P), 2):
        MR[P[i]], MR[P[i+1]] = P[i+1], P[i]
    return MR