from dados import carregar_dados, salvar_dados, estatisticas
from utils import nova_carta, valor_mao, mostrar_mao

# Executa uma rodada completa do jogo de Blackjack
def rodada(dados):
    """
        Executa uma rodada completa do jogo:
        1. Exibe saldo e solicita aposta
        2. Distribui cartas para o jogador e o dealer
        3. Mostra as cartas do jogador e uma do dealer
        4. Loop de ações do jogador (hit, stand, double)
        5. Jogada automática do dealer
        6. Verifica o resultado da rodada e atualiza o saldo
    """

    # --- 1. Exibe saldo e solicita aposta ---
    saldo = dados["saldo"]
    print(f"\nSeu saldo atual: R${saldo:.2f}")

    # Solicita aposta, até ser dada uma aposta válida
    while True:
        try:
            aposta = float(input("Digite o valor da aposta: R$"))
            if aposta <= 0:
                print("👉 A aposta deve ser maior que zero.")
            elif aposta > saldo:
                print(f"👉 Você não pode apostar mais do que o saldo disponível: R${saldo:.2f}")
            else:
                break
        except ValueError:
            print("👉 Valor inválido. Tente novamente.")
    
    # --- 2) Distribui cartas para o jogador e o dealer ---
    jogador = [nova_carta(), nova_carta()]
    dealer = [nova_carta(), nova_carta()]

    # --- 3) Mostra as cartas do jogador e uma do dealer ---
    print(f"Sua mão: {mostrar_mao(jogador,      ocultar=False)}")
    print(f"Mão do dealer: {mostrar_mao(dealer, ocultar=True)}")

    # --- 4) Loop de ações do jogador (hit, stand, double) ---
    # Enquanto o valor do jogador for inferior a 21, oferecemos as opções de ação
    while  valor_mao(jogador) < 21:
        print("\nEscolha uma ação:")
        print("[h] Pedir carta (hit)")
        print("[s] Parar (stand)")
        print("[d] Dobrar aposta (double)")
        acao = input("> ").strip().lower()      # Lê a ação do jogador, removendo espaços e convertendo para minúsculas

        if acao == "h":
            jogador.append(nova_carta())        # Adiciona uma nova carta à mão do jogador
            print(f"Sua mão: {mostrar_mao(jogador)}")
        elif acao == "d":
            if aposta * 2 > dados["saldo"]:     # Verifica se o jogador tem saldo suficiente para dobrar a aposta
                print("👉 Saldo suficiente.")
                continue
            aposta *= 2
            jogador.append(nova_carta())
            print(f"Sua mão: {mostrar_mao(jogador)}")
            break                               # Após o double, o jogador não pode pedir mais cartas
        elif acao == "s":
            break                               # O jogador opta por parar, saindo do loop
        else:
            print("👉 Ação inválida. Tente novamente.")
    
    # --- 5) Jogada automática do dealer ---
    print(f"\nMão do dealer: {mostrar_mao(dealer, ocultar=False)}")
    
    # O dealer deve continuar a jogar até atingir 17 ou mais
    while valor_mao(dealer) < 17:
        dealer.append(nova_carta())
        print(f"Mão do dealer: {mostrar_mao(dealer, ocultar=False)}")
    
    # --- 6) Verifica o resultado da rodada e atualiza o saldo ---
    total_j = valor_mao(jogador)
    total_d = valor_mao(dealer)
    print(f"\nSeus pontos: {total_j}")
    print(f"\nPontos do dealer: {total_d}")

    # Verifica se o jogador ganhou, perdeu ou empatou e atualiza os dados
    if total_j > 21:
        print("❌ Você estourou! Perdeu a rodada.")
        dados["saldo"] -= aposta
        dados["derrotas"] += 1
    elif total_d > 21 or total_j > total_d:
        print("✅ Você ganhou a rodada!")
        dados["saldo"] += aposta
        dados["vitorias"] += 1
    elif total_j == total_d:
        print("🤝 Empate!")
        dados["empates"] += 1
    else:
        print("❌ Você perdeu a rodada.")
        dados["saldo"] -= aposta
        dados["derrotas"] += 1

# Executa o menu e o loop principal do jogo
def main():
    dados = carregar_dados()  # Carrega os dados do jogo (saldo, vitórias, derrotas, empates)

    print("Bem-vindo ao jogo de Blackjack!")

    # Loop principal do jogo
    while True:
        # Menu do jogo
        print("\nEscolha uma opção:")
        print("[1] Jogar uma rodada")
        print("[2] Ver estatísticas")
        print("[3] Sair do jogo")
        # Solicita a opção do jogador
        opcao = input("Escolha uma opção: ").strip()

        # Verifica a opção escolhida
        if opcao == "1":
            rodada(dados)
            salvar_dados(dados)  # Salva os dados após cada rodada
        elif opcao == "2":
            estatisticas(dados)  # Exibe as estatísticas do jogador
        elif opcao == "3":
            salvar_dados(dados)  # Salva os dados antes de sair
            print("Obrigado por jogar! Até a próxima.")
            break
        else:
            print("👉 Opção inválida. Tente novamente.")

if __name__ == "__main__":
    # O "if __name__ == "__main__":" é uma convenção em Python que permite que
    # o código dentro do bloco seja executado apenas se o arquivo for executado
    # diretamente, e não quando importado como um módulo em outro arquivo.
  
    main()  # Inicia o jogo chamando a função principal