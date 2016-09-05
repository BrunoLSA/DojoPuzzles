"""
Desenvolva um programa que simule a entrega de notas quando um cliente efetuar um saque em um caixa eletrônico. Os requisitos básicos são os seguintes:
Entregar o menor número de notas;
É possível sacar o valor solicitado com as notas disponíveis;
Saldo do cliente infinito;
Quantidade de notas infinito (pode-se colocar um valor finito de cédulas para aumentar a dificuldade do problema);
Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00
Exemplos:
Valor do Saque: R$ 30,00 – Resultado Esperado: Entregar 1 nota de R$20,00 e 1 nota de R$ 10,00.
Valor do Saque: R$ 80,00 – Resultado Esperado: Entregar 1 nota de R$50,00 1 nota de R$ 20,00 e 1 nota de R$ 10,00.
"""

def notas(valor):
    notaDez = 0
    notaVinte = 0
    notaCinquenta = 0
    notaCem = 0

    if not valor % 10 == 0:
        return "Valor inválido. Digite um valor múltiplo de 10."
    if valor > 100:
        notaCem = valor//100
        valor = valor % 100
    if valor > 50:
        notaCinquenta = valor//50
        valor = valor % 50
    if valor > 20:
        notaVinte = valor//20
        valor = valor % 20
    notaDez = valor//10

    return "Entregar %d nota(s) de R$ 100,00, %d nota(s) de R$ 50,00, %d nota(s) de R$ 20,00 e %d nota(s) de 10,00." % (notaCem, notaCinquenta, notaVinte, notaDez)


#Testes:
assert notas(10) == "Entregar 0 nota(s) de R$ 100,00, 0 nota(s) de R$ 50,00, 0 nota(s) de R$ 20,00 e 1 nota(s) de 10,00."
assert notas(30) == "Entregar 0 nota(s) de R$ 100,00, 0 nota(s) de R$ 50,00, 1 nota(s) de R$ 20,00 e 1 nota(s) de 10,00."
assert notas(80) == "Entregar 0 nota(s) de R$ 100,00, 1 nota(s) de R$ 50,00, 1 nota(s) de R$ 20,00 e 1 nota(s) de 10,00."
assert notas(190) == "Entregar 1 nota(s) de R$ 100,00, 1 nota(s) de R$ 50,00, 2 nota(s) de R$ 20,00 e 0 nota(s) de 10,00."
assert notas(25) == "Valor inválido. Digite um valor múltiplo de 10."