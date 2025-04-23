# Importamos o módulo json para manipular arquivos JSON
# Importamos o módulo os para manipular caminhos de arquivos
import json
import os

# Importa a função que calcula o valor da mão do jogador
from utils import valor_mao

ARQUIVO_SALDO = 'saldo.json'

# Função para carregar o saldo do arquivo JSON
def carregar_dados():
    """
    Lê o arquivo saldo.json e retorna os dados como um dicionário:
    - saldo: Saldo atual do jogador (float ou int)
    - vitorias: Número de vitórias (int)
    - derrotas: Número de derrotas (int)
    - empates: Número de empates (int)
    """
    
    # 1. Verifica se o arquivo existe no disco
    if os.path.exists(ARQUIVO_SALDO):
        # 2. Se o arquivo existe, abre o arquivo e carrega os dados
        with open(ARQUIVO_SALDO, 'r') as f:
                # "r" indica que o arquivo será aberto para leitura.
            # 3. Carrega os dados do arquivo JSON para um dicionário Python e retorna
            return json.load(f)
    
    # 4. Se o arquivo não existe, retorna um dicionário com valores padrão
    return {
        "saldo": 1000,
        "vitorias": 0,
        "derrotas": 0,
        "empates": 0
    }

# Função para salvar o saldo no arquivo JSON
def salvar_dados(dados):
    """
    Recebe um dicionário com os dados do jogador e salva no arquivo saldo.json.
    """
    # 1. Abre o arquivo saldo.json para escrita
    with open(ARQUIVO_SALDO, "w") as f:
            # O "w" indica que o arquivo será aberto para escrita, e se já existir, será sobrescrito.
        # 2. Converte o dicionário para JSON e escreve no arquivo
        json.dump(dados, f, indent=2)
            # "ident=2" formata o JSON com 2 espaços de indentação, para facilitar a leitura humana

# Função para uma visualização mais bonita do saldo
def estatisticas(dados):
    """
    Recebe o dicionário 'dados' e exibe:
      - Saldo atual
      - Número de vitórias, derrotas e empates
      - Taxa de vitória em %
    """
    # 1) Extrair valores do dicionário
    saldo   = dados["saldo"]
    vitorias = dados["vitorias"]
    derrotas = dados["derrotas"]
    empates  = dados["empates"]

    # 2) Calcular total de jogos
    total_jogos = vitorias + derrotas + empates

    # 3) Calcular taxa de vitória (evitar divisão por zero)
    if total_jogos > 0:
        taxa_vitoria = (vitorias / total_jogos) * 100
    else:
        taxa_vitoria = 0.0

    # 4) Exibir informações de forma formatada
    print("\n=== ESTATÍSTICAS ===")
    print(f"Saldo atual:       R$ {saldo}")
    print(f"Partidas jogadas:  {total_jogos}")
    print(f"  • Vitórias:      {vitorias}")
    print(f"  • Derrotas:      {derrotas}")
    print(f"  • Empates:       {empates}")
    print(f"Taxa de vitória:   {taxa_vitoria:.2f}%")
    print("====================\n")
