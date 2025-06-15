import random

def criar_tabuleiro():
    """Cria um tabuleiro vazio do jogo da velha"""
    return [" " for _ in range(9)]

def exibir_tabuleiro(tabuleiro):
    """Exibe o tabuleiro na tela"""
    print("\n")
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("-----------")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("-----------")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")
    print("\n")

def verificar_vitoria(tabuleiro, jogador):
    """Verifica se o jogador venceu"""
    # Verifica linhas, colunas e diagonais
    combinacoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # colunas
        [0, 4, 8], [2, 4, 6]              # diagonais
    ]
    
    for combo in combinacoes:
        if all(tabuleiro[pos] == jogador for pos in combo):
            return True
    return False

def verificar_empate(tabuleiro):
    """Verifica se o jogo terminou em empate"""
    return " " not in tabuleiro

def jogada_jogador(tabuleiro, jogador):
    """Solicita e valida a jogada do jogador humano"""
    while True:
        try:
            posicao = int(input(f"Jogador {jogador}, escolha uma posição (1-9): ")) - 1
            if 0 <= posicao <= 8 and tabuleiro[posicao] == " ":
                return posicao
            else:
                print("Posição inválida ou já ocupada. Tente novamente.")
        except ValueError:
            print("Por favor, digite um número entre 1 e 9.")

def jogada_computador(tabuleiro, jogador):
    """Lógica simples para a jogada do computador"""
    # Primeiro, verifica se pode vencer na próxima jogada
    for i in range(9):
        if tabuleiro[i] == " ":
            tabuleiro_copia = tabuleiro.copy()
            tabuleiro_copia[i] = jogador
            if verificar_vitoria(tabuleiro_copia, jogador):
                return i
    
    # Depois, verifica se o oponente pode vencer e bloqueia
    oponente = "O" if jogador == "X" else "X"
    for i in range(9):
        if tabuleiro[i] == " ":
            tabuleiro_copia = tabuleiro.copy()
            tabuleiro_copia[i] = oponente
            if verificar_vitoria(tabuleiro_copia, oponente):
                return i
    
    # Tenta jogar no centro
    if tabuleiro[4] == " ":
        return 4
    
    # Tenta jogar nos cantos
    cantos = [0, 2, 6, 8]
    cantos_disponiveis = [c for c in cantos if tabuleiro[c] == " "]
    if cantos_disponiveis:
        return random.choice(cantos_disponiveis)
    
    # Joga em qualquer posição disponível
    posicoes_disponiveis = [i for i in range(9) if tabuleiro[i] == " "]
    return random.choice(posicoes_disponiveis)

def jogar_contra_pessoa():
    """Modo de jogo: jogador contra jogador"""
    tabuleiro = criar_tabuleiro()
    jogador_atual = "X"
    
    while True:
        exibir_tabuleiro(tabuleiro)
        posicao = jogada_jogador(tabuleiro, jogador_atual)
        tabuleiro[posicao] = jogador_atual
        
        if verificar_vitoria(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f"Parabéns! Jogador {jogador_atual} venceu!")
            break
        
        if verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("Empate! O jogo terminou sem vencedor.")
            break
        
        jogador_atual = "O" if jogador_atual == "X" else "X"

def jogar_contra_computador():
    """Modo de jogo: jogador contra computador"""
    tabuleiro = criar_tabuleiro()
    
    # O jogador escolhe X ou O
    while True:
        escolha = input("Você quer ser X ou O? (X começa) ").upper()
        if escolha in ["X", "O"]:
            jogador_humano = escolha
            jogador_computador = "O" if escolha == "X" else "X"
            break
        else:
            print("Escolha inválida. Digite X ou O.")
    
    jogador_atual = "X"  # X sempre começa
    
    while True:
        exibir_tabuleiro(tabuleiro)
        
        if jogador_atual == jogador_humano:
            posicao = jogada_jogador(tabuleiro, jogador_atual)
        else:
            print("Vez do computador...")
            posicao = jogada_computador(tabuleiro, jogador_computador)
        
        tabuleiro[posicao] = jogador_atual
        
        if verificar_vitoria(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            if jogador_atual == jogador_humano:
                print("Parabéns! Você venceu!")
            else:
                print("O computador venceu!")
            break
        
        if verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("Empate! O jogo terminou sem vencedor.")
            break
        
        jogador_atual = jogador_computador if jogador_atual == jogador_humano else jogador_humano

def menu_principal():
    """Exibe o menu principal e gerencia as opções"""
    while True:
        print("\n--- Jogo da Velha ---")
        print("1. Jogar contra outra pessoa")
        print("2. Jogar contra o computador")
        print("3. Sair")
        
        opcao = input("Escolha uma opção (1-3): ")
        
        if opcao == "1":
            jogar_contra_pessoa()
        elif opcao == "2":
            jogar_contra_computador()
        elif opcao == "3":
            print("Obrigado por jogar! Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

if __name__ == "__main__":
    menu_principal()