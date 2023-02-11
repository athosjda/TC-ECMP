from Grafo import Grafo

def emparelhamento_geral(G:Grafo):
    M = [None]*(G.n+1)
    while True:
        P = reducao_blossom(G, M)
        M = diferenca_simetrica(M, P) # conferir a implementação da diferença simétrica
        if len(P) == 0:
            break
    return M

def reducao_blossom(G:Grafo, M):
    (P, F, H) = aumentante()
    if len(P) > 0 and F != None:
        (GF, MF) = obter_GFMF(G, M, F, H)
        Plin = reducao_blossom(GF, MF)
        P = contrucao_1(G, GF, F, H, M, Plin)
    return P

def aumente(G:Grafo, M):
    Df = Grafo(G.n)
    Df.expressao_associada = [None]*(Df.n+1)
    for v in G.vertex:
        for w in G.adj[v]:
            if M[w] != v:
                if M[w] == None:
                    Df.expressao_associada[v] = w
                else:
                    e =  Df.inserir_arestas(v, M[w])
                    # e.inter = w  # Conferir na bibliografia a estrutura de grafos como é definido um Nó
    
    Df.Exp = [True]*(Df.n+1) 
    for v in M:
        if v != None:
            Df.Exp[v] = False
    Pf = BuscaCaminhoAumentante(Df)
    (P, F, H) = construcao_3(Pf, Df, G, M)

    return(P, F, H)

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