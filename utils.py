# Importação da biblioteca que permite gerar números aleatórios
import random

# Função para gerar uma carta aleatória
def nova_carta():
    """
    Retorna um valor aleatório que representa uma carta de Blackjack.
        - 2 a 10: cartas com valores numéricos
        - 10: Valete, Dama e Rei (todos valem 10)
        - 11: Ás (pode valer 1 ou 11, o que será definido na lógica do jogo)
    """

    # Lista de cartas com seus respectivos valores
    cartas = [
        2, 3, 4, 5, 6, 7, 8, 9, 10, # cartas numéricas
        10, 10, 10, 10,  # Valete, Dama e Rei
        11  # Ás
    ]
    # Retorna uma carta aleatória da lista
    return random.choice(cartas)

# Função para calcular o valor total da mão do jogador
def valor_mao(mao):
    """
    Receve uma lista de inteiros (a mão do jogador) e retorna o valor total da mão.

    Se o valor passar de 21, converte os ases para  1, até que o valor fique abaixo de 21.
    """

    total = sum(mao)        # soma todos os valores, contando cada Ás como 11
    ases = mao.count(11)    # conta quantos Ases estão na mão

    # Enquanto a soma total de pontos for maior que 21 e houver Ases na mão valendo 11
    # Transforma cada Ás de 11 em 1 (subtraindo 10 do total)
    # Isso é feito para evitar que o jogador estoure (ultrapasse 21)
    while total > 21 and ases:
        total -= 10     # Transforma o valor do Às de 11 para 1
        ases -= 1       # Diminui a contagem de Ases
    return total

# Função para mostrar a mão do jogador, ocultar ou não
def mostrar_mao(mao, ocultar=False):
    """
        Retorna uma string que mostra a mão do jogador e, opcionalmente, o valor:
        - Se ocultar for True, mostra a primeira carta e um ponto de interrogação.
        - Se ocultar for False, mostra todas as cartas e o valor total.
        
        mao: lista de inteiros representando a mão do jogador
        ocultar: booleano que indica se a mão deve ser mostrada ou não
    """

    if ocultar:
        # mostra apenas a carta na posiçã 0 e um "?"
        return f"[{mao[0]}, ?]"
    else:
        # mostra todas as cartas e o valor total
        valor = valor_mao(mao)
        return f"{mao} = {valor}"
