"""
Para definir uma seqüência a partir de um número inteiro o positivo, temos as seguintes regras:
n → n/2 (n é par)
n → 3n + 1 (n é ímpar)
Usando a regra acima e iniciando com o número 13, geramos a seguinte seqüência:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
Podemos ver que esta seqüência (iniciando em 13 e terminando em 1) contém 10 termos. Embora ainda não tenha sido provado (este problema é conhecido como Problema de Collatz), sabemos que com qualquer número que você começar, a seqüência resultante chega no número 1 em algum momento.
Desenvolva um programa que descubra qual o número inicial entre 1 e 1 milhão que produz a maior seqüência.
"""


def next_(n):
    '''Return the next number for the sequence.'''
    return (3 * n + 1) if n % 2 else (n // 2)


def seq(n):
    '''Generator to produce a complete sequence from n.'''
    yield n

    while n > 1:
        n = next_(n)
        yield n


def count(iterable):
    '''Return how many elements has an iterable.'''
    return sum(1 for _ in iterable)


def max_length(start=1, stop=1000001):
    '''Returns the number and length of the longest sequence.'''
    length, number = max((count(seq(n)), n) for n in range(start, stop))
    return number, length


# Tests
assert next_(1) == 4
assert next_(2) == 1
assert next_(13) == 40

assert list(seq(13)) == [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
assert count(seq(13)) == 10

assert max_length(1, 14) == (9, 20)  # number 9, length 20

print(max_length(start=1, stop=1000001))
