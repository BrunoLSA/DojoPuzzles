"""
O sistema de numeração romana (ou números romanos) desenvolveu-se na Roma Antiga e
utilizou-se em todo o seu Império. Neste sistema as cifras escrevem-se com determinadas
letras, que representam os números. As letras são sempre maiúsculas, já que no alfabeto
romano não existem as minúsculas, as letras são I, V, X, L, C, D e M.

Sua tarefa é desenvolver um programa que converta números indo-arábicos para o formato
romano e vice-versa. As regras para a formação dos números romanos são apresentadas a
seguir.

Cada letra corresponde a um determinado valor:
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

Agrupando as letras acima, podemos representar os números de acordo com um conjunto de regras:
Com exceção de V, L e D, os outros numerais podem se repetir no máximo três vezes:
III = 3
XXX = 30
CCC = 300
MMM = 3000

Quando escritos à direita de numerais maiores, I, X e C somam-se aos valores dos primeiros:
VIII = 5 + 1 + 1 + 1 = 8
LXII = 50 + 10 + 1 + 1 = 62
CLVIII = 158
MCXX = 1000 + 100 + 10 + 10 = 1120

Mas se os numerais I, X e C estiverem à esquerda dos maiores, seus valores são subtraídos como, por exemplo, em:
IV = 5 - 1 = 4
IX = 10 - 1 = 9
XC = 100 - 10 = 90
"""


def romano(a):
    if a >= 4000:
        return "Número inválido. Digite um número menor que 4.000."
    else:
        n = a

        m = n // 1000
        n = n - 1000 * m

        d = n // 500
        n = n - 500 * d

        c = n // 100
        n = n - 100 * c

        l = n // 50
        n = n - 50 * l

        x = n // 10
        n = n - 10 * x

        v = n // 5
        n = n - 5 * v

        i = n

        romano = m * "M" + d * "D" + c * "C" + l * "L" + x * "X" + v * "V" + i * "I"

        if romano[-4:] == "IIII" and len(romano) == 4:
            romano = "IV"
        if romano[-4:] == "IIII" and len(romano) > 4 and romano[-5] != "V":
            romano = romano[:-4] + "IV"
        if romano[-4:] == "IIII" and len(romano) > 4 and romano[-5] == "V":
            romano = romano[:-5] + "IX"

        find_x = romano.find("XXXX")
        if "XXXX" in romano and find_x == 0:
            romano = "XL" + romano[4:]
        elif "XXXX" in romano and len(romano) > 4 and romano[find_x - 1] == "L":
            romano = romano[:find_x - 1] + "XC" + romano[find_x + 4:]
        elif "XXXX" in romano and len(romano) > 4 and romano[find_x - 1] != "L":
            romano = romano[:find_x] + "XL" + romano[find_x + 4:]

        find_c = romano.find("CCCC")
        if "CCCC" in romano and find_c == 0:
            romano = "CD" + romano[4:]
        elif "CCCC" in romano and len(romano) > 4 and romano[find_c - 1] == "D":
            romano = romano[:find_c - 1] + "CM" + romano[find_c + 4:]
        elif "CCCC" in romano and len(romano) > 4 and romano[find_c - 1] != "D":
            romano = romano[:find_c] + "CD" + romano[find_c + 4:]

        return str(a) + " = " + romano

def arabic(n):
    romano = n.upper()
    arabic = 0

    if "M" in romano:
        if "CM" in romano:
            arabic += 900
            romano = "".join(romano.split("CM"))
        arabic += 1000 * romano.count("M")
        romano = romano[romano.rfind("M") + 1:]

    if "D" in romano:
        if romano[0] == "C":
            arabic += 400
        else:
            arabic += 500
        romano = romano[romano.find("D") + 1:]

    if "C" in romano:
        if "XC" in romano:
            arabic += 90
            romano = "".join(romano.split("XC"))
        arabic += 100 * romano.count("C")
        romano = romano[romano.rfind("C") + 1:]

    if "L" in romano:
        if romano[0] == "X":
            arabic += 40
        else:
            arabic += 50
        romano = romano[romano.find("L") + 1:]

    if "X" in romano:
        if "IX" in romano:
            arabic += 9
            romano = "".join(romano.split("IX"))
        arabic += 10 * romano.count("X")
        romano = romano[romano.rfind("X") + 1:]

    if "V" in romano:
        if "IV" in romano:
            arabic += 4
        else:
            arabic += 5
        romano = romano[romano.find("V") + 1:]

    if "I" in romano:
        arabic += romano.count("I")

    return n + " = " + str(arabic)



#Tests:
assert romano(3) == "3 = III"
assert romano(30) == "30 = XXX"
assert romano(300) == "300 = CCC"
assert romano(500) == "500 = D"
assert romano(499) == "499 = CDXCIX"
assert romano(3400) == "3400 = MMMCD"
assert romano(5000) == "Número inválido. Digite um número menor que 4.000."

assert arabic("MMCCCXLVIII") == "MMCCCXLVIII = 2348"
assert arabic("MMCCCXLIX") == "MMCCCXLIX = 2349"
assert arabic("MMMCCCXCIV") == "MMMCCCXCIV = 3394"
assert arabic("MMMCCXCVII") == "MMMCCXCVII = 3297"
assert arabic("MCMXCIX") == "MCMXCIX = 1999"
assert arabic("MCDXCIV") == "MCDXCIV = 1494"
assert arabic("XXXIX") == "XXXIX = 39"
assert arabic("I") == "I = 1"



