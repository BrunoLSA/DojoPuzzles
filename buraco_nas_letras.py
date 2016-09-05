"""
Se você pensar em um papel como um plano e uma letra como uma marcação neste plano,
então estas letras dividem o plano em regiões. Por exemplo, as letras A, D e O dividem
o plano em 2 pois possuem um espaço confinado em seu desenho, ou um “buraco”. Outras
letras como B possuem 2 buracos e letras como C e E não possuem buracos.

Deste modo podemos considerar que o número de buracos em um texto é igual a soma dos
buracos nas palavras dele.

A sua tarefa é, dado um texto qualquer, encontre a quantidade de buracos nele.
"""

def numBuracos(texto):
    um_buraco = ["A", "D", "O", "P", "Q", "R", "a", "b", "d", "e", "g", "o", "p", "q"]
    b = 0
    for t in texto:
        if t in um_buraco:
            b += 1
        if t == "B":
            b += 2
        else:
            pass
    return b


#Testes:
assert numBuracos("Carro") == 2
assert numBuracos("software") == 3
assert numBuracos("This house is very big") == 5
assert numBuracos("Welcome to the Django - a arte de ser feliz programando") == 23