"""
Para definir uma seqüência a partir de um número inteiro o positivo, temos as seguintes regras:
n → n/2 (n é par)
n → 3n + 1 (n é ímpar)
Usando a regra acima e iniciando com o número 13, geramos a seguinte seqüência:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
Podemos ver que esta seqüência (iniciando em 13 e terminando em 1) contém 10 termos. Embora ainda não tenha sido provado (este problema é conhecido como Problema de Collatz), sabemos que com qualquer número que você começar, a seqüência resultante chega no número 1 em algum momento.
Desenvolva um programa que descubra qual o número inicial entre 1 e 1 milhão que produz a maior seqüência.
"""

def seq(number):
    l = [number]
    while l[-1] != 1:
        if l[-1]%2 == 0:
            l.append(l[-1]//2)
        else:
            l.append(3*l[-1] + 1)
    return len(l)

def discover():
    l2 = []
    for i in range(1, 1000000):
        l2.append(seq(i))
    return l2.index(max(l2)) + 1



#Testes:
assert seq(4) == 3
assert seq(5) == 6
assert seq(13) == 10

print(discover())
