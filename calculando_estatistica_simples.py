"""
Sua tarefa é processar uma seqüência de números inteiros para
determinar as seguintes estatísticas:
Valor mínimo
Valor máximo
Número de elementos na seqüência
Valor médio

Por exemplo para uma seqüência de números "6, 9, 15, -2, 92, 11",
temos como saída:
Valor mínimo: -2
Valor máximo: 92
Número de elementos na seqüência: 6
Valor médio: 21.83333
"""
def estat(list):
    return "Valor mínimo: %s \nValor máximo: %s \nNúmero de elementos na sequência: %s \nValor médio: %s" % (str(min(list)), str(max(list)), str(len(list)), str((sum(list)/len(list))))

lista_1 = [6, 9, 15, -2, 92, 11]
lista_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lista_3 = [1]
lista_4 = [-3, -4, -70, 66, -99999, 1.03, 42, 40, 0.123]


assert estat(lista_1) == "Valor mínimo: -2 \nValor máximo: 92 \nNúmero de elementos na sequência: 6 \nValor médio: 21.833333333333332"
assert estat(lista_2) == "Valor mínimo: 0 \nValor máximo: 0 \nNúmero de elementos na sequência: 10 \nValor médio: 0.0"
assert estat(lista_3) == "Valor mínimo: 1 \nValor máximo: 1 \nNúmero de elementos na sequência: 1 \nValor médio: 1.0"
assert estat(lista_4) == "Valor mínimo: -99999 \nValor máximo: 66 \nNúmero de elementos na sequência: 9 \nValor médio: -11102.983"

