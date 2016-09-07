"""
Um homem chamado José é o responsável por ligar e desligar as luzes de um corredor.
Cada lâmpada tem seu próprio interruptor que liga e a desliga. Inicialmente todas as
lâmpadas estão desligadas.

José faz uma coisa peculiar: se existem n lâmpadas no corredor, ele caminha até o fim
do corredor e volta n vezes. Na iésima caminhada, ele aperta apenas os interruptores
aos quais sua posição é divisível por i. Ele não aperta nenhum interruptor na volta à
sua posição inicial, apenas na ida. A iésima caminhada é definida como ir ao fim do
corredor e voltar.

Determine qual é o estado final de cada lâmpada. Está ligada ou desligada?

Exemplo:
Entrada: 3
Saída: [on, off, off]
"""


def lampada(n):
    status = (n+1)*["off"]
    for i in range(1, n+1):
        for a in range(1, n+1):
            if a % i == 0 and status[a] == "on":
                status[a] = "off"
            elif a % i == 0 and status[a] == "off":
                status[a] = "on"
            else:
                pass
    del status[0]
    return status


#Tests:
assert lampada(3) == ["on", "off", "off"]
assert lampada(2) == ["on", "off"]
assert lampada(4) == ["on", "off", "off", "on"]
assert lampada(5) == ["on", "off", "off", "on", "off"]
