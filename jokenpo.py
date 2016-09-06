"""
Jokenpo é uma brincadeira japonesa, onde dois jogadores escolhem um dentre três possíveis itens: Pedra, Papel ou Tesoura.
O objetivo é fazer um juiz de Jokenpo que dada a jogada dos dois jogadores informa o resultado da partida.
As regras são as seguintes:
Pedra empata com Pedra e ganha de Tesoura
Tesoura empata com Tesoura e ganha de Papel
Papel empata com Papel e ganha de Pedra
"""

def jokenpo(a, b):
    if a == b:
        return "empate"
    else:
        if a == "pedra":
            return "pedra" if b == "tesoura" else "papel"
        elif a == "tesoura":
            return "tesoura" if b == "papel" else "pedra"
        elif a == "papel":
            return "papel" if b == "pedra" else "tesoura"

assert jokenpo("pedra", "pedra") == "empate"
assert jokenpo("pedra", "tesoura") == "pedra"
assert jokenpo("tesoura", "tesoura") == "empate"
assert jokenpo("tesoura", "papel") == "tesoura"
assert jokenpo("papel", "papel") == "empate"
assert jokenpo("papel", "pedra") == "papel"