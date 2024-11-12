import random

def computador_joga(fosforos):
    jogada = (fosforos - 1) % 5
    if jogada == 0:
        jogada = random.randint(1, 4)
    print(f"O computador tirou {jogada} fósforos.")
    return jogada

def jogador_joga(fosforos):
    while True:
        try:
            jogada = int(input("Quantos fósforos você quer tirar? (1-4): "))
            if jogada in [1, 2, 3, 4]:
                return jogada
            else:
                print("Jogada inválida. Escolha um número entre 1 e 4.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número entre 1 e 4.")

def modo_jogador_primeiro():
    fosforos = 21
    while fosforos > 0:
        jogada_jogador = jogador_joga(fosforos)
        fosforos = fosforos - jogada_jogador
        print(f"Restam {fosforos} fósforos.")
        if fosforos <= 0:
            print("Você tirou o último fósforo. Perdeu!")
            return

        jogada_computador = computador_joga(fosforos)
        fosforos = fosforos - jogada_computador
        print(f"Restam {fosforos} fósforos.")
        if fosforos <= 0:
            print("O computador tirou o último fósforo. Você ganhou!")
            return

def modo_computador_primeiro():
    fosforos = 21
    while fosforos > 0:
        jogada_computador = computador_joga(fosforos)
        fosforos = fosforos - jogada_computador
        print(f"Restam {fosforos} fósforos.")
        if fosforos <= 0:
            print("O computador tirou o último fósforo. Você ganhou!")
            return

        jogada_jogador = jogador_joga(fosforos)
        fosforos = fosforos - jogada_jogador
        print(f"Restam {fosforos} fósforos.")
        if fosforos <= 0:
            print("Você tirou o último fósforo. Perdeu!")
            return

def jogo():
    print("Bem-vindo ao jogo dos 21 fósforos!")
    print("Quem tirar o último fósforo perde o jogo.")

    while True:
        print("Escolha o modo de jogo (1 ou 2).")
        print("1 - Você começa.")
        print("2 - O computador começa.")
        modo = input("Digite o número do modo: ")

        if modo == '1':
            modo_jogador_primeiro()
            break
        elif modo == '2':
            modo_computador_primeiro()
            break
        else:
            print("Opção inválida. Tente novamente.")

jogo()