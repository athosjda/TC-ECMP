from teste import fatorail


def distancia_hamming(s1, s2):
    assert len(s1) == len(s2)
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

def fatorial(n):
    if n <= 0:
        return 0
    soma = 1
    for i in range(1, n+1):
        soma *= i
    return soma

def binomio_newton(n, p):
    return fatorial(n)/(fatorial(p)*fatorail(n-p))
