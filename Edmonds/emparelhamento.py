from Grafo import Grafo

def emparelhamento_geral(G:Grafo):
    M = [None]*(G.n+1)
    while True:
        P = reducao_blossom()
        M = DifSimetrica() # conferir a implementação da diferença simétrica
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
    for v in G.vertex:
        for w in G.adj[v]:
            if M[w] != v:
                if M[w] == None:
                    continue # Conferir na bibliografia
                else:
                    e =  Df.inserir_arestas(v, M[w])
                    # e.inter = w # Conferir na bibliografia
    
    # Df.Exp = [True]*(Df.n) # Conferir na bibliografia a estrutura de grafos
    for v in M:
        if v != None:
            #Df.Exp[v] = False
    Pf = BuscaCaminhoAumentante()
    (P, F, H) = construcao_3(Pf, Df, G, M)

    return(P, F, H)

    def construcao_3(Pf, Df, G, M):
        Ciclo = None 
        H = None

        VMarcado = [-1]*(Df.n+1)
        i = 0
        for v in Pf:
            if VMarcado[v] > -1:
                ciclo = pf[VMarcado[v]:i]
                H = Pf[:VMarcado[v]+1]
                break
            else:
                VMarcado[v] = i
                i = i+1
        return (Pf, Ciclo, H)