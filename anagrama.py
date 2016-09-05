"""
Escreva um programa que gere todos os anagramas potenciais de uma string.
Por exmplo, os anagramas potenciais de "biro" são:
biro bior brio broi boir bori
ibro ibor irbo irob iobr iorb
rbio rboi ribo riob roib robi
obir obri oibr oirb orbi orib
"""

from itertools import permutations

def anagrama(word):
    return list("".join(t) for t in permutations(word))


#Testes:
assert anagrama("word") == ["word", "wodr", "wrod", "wrdo", "wdor", "wdro",
                            "owrd", "owdr", "orwd", "ordw", "odwr", "odrw",
                            "rwod", "rwdo", "rowd", "rodw", "rdwo", "rdow",
                            "dwor", "dwro", "dowr", "dorw", "drwo", "drow"]
assert anagrama("and") == ["and", "adn", "nad", "nda", "dan", "dna"]
assert anagrama("go") == ["go", "og"]
