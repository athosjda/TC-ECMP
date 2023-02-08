from Grafo import Grafo

def emparelhamento_geral(G:Grafo):
    M = [None]*(G.n+1)
    while True:
        P = reducao_blossom()
        M = DifSimetrica()
        if len(P) == 0:
            break
    return M

def reducao_blossom(G:Grafo, M):
    (P, F, H) = caminho_aumentante()
    if len(P) > 0 and F != None:
        (GF, MF) = obter_GFMF(G, M, F, H)
        Plin = reducao_blossom(GF, MF)
        P = contrucao_1(G, GF, F, H, M, Plin)
    return P

def caminho_aumente(G:Grafo, M):
    Df = Grafo(G.n)
    for v in G.vertex:
        for w in G.adj[v]:
            if M[w] != v:
                if M[w] == None:
                    continue # Conferir na bibliografia
                else:
                    e =  Df.inserir_arestas(v, M[w])
                    # e.inter = w # Conferir na bibliografia