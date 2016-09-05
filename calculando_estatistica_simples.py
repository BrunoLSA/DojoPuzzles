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
Valor médio: 18.1666666
"""
def estat(list):
    return "Valor mínimo: %d \nValor máximo: %d \nNúmero de elementos na sequência: %d \nValor médio: %f" % (min(list), max(list), len(list), (sum(list)/len(list)))

print(estat([6, 9, 15, -2, 92, 11]))
