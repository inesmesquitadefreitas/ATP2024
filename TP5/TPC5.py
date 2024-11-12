# Definir as funções

# Verifica se uma certa sala existe
def Existe_Sala(cinema, s):
    cond = False
    for sala in cinema:
        nlugares, vendidos, filme = sala
        if sala[2] == s[2]:
            cond = True
    return cond

# Insere a sala na lista "cinema", apenas se esta ainda não existir nessa lista (para evitar repetições)
def Inserir_Sala(cinema, s):
    if not Existe_Sala(cinema, s):
        cinema.append(s)
    else: print(f"A sala com o filme '{s[2]}' já existe.")
    return cinema


# Lista no monitor todos os filmes que estão em exibição nas salas do cinema
def Listar(cinema):
    print (" ----- FILMES EM EXIBIÇÃO ----- ")
    for sala in cinema:
        nlugares, vendidos, filme = sala
        print (f" {filme}")
    print (" ------------------------------ ")

# Indica se um certo lugar está disponível ou não
def Disponivel(cinema, nome_filme, lugar):
    cond = False
    for sala in cinema:
        nlugares, vendidos, filme = sala
        if nome_filme == filme and lugar <= nlugares:
            if lugar not in vendidos:
                cond = True
    return cond

# Vende um bilhete e adiciona o respetivo lugar à lista "vendidos"
def Vende_Bilhete(cinema, nome_filme, lugar):
    if Disponivel(cinema, nome_filme, lugar):
        for sala in cinema:
            nlugares, vendidos, filme = sala
            if nome_filme == filme:
                if lugar not in vendidos:
                    vendidos.append(lugar)
    return cinema

# Lista no monitor o número de lugares ainda disponíveis de cada filme
def Listar_Disponibilidades(cinema):
    print("FILMES | LUGARES DISPONÍVEIS")
    for sala in cinema:
        nlugares, vendidos, filme = sala
        disponiveis = nlugares - len(vendidos)    
        print (f"{filme}  |  {disponiveis}    ")
    return cinema

# Remove uma certa sala
def Remover_Sala(cinema, filme):
    return[sala for sala in cinema if sala[2] != filme]


# Definir o Menu
def Menu():
    cinema = []
    
    while True:
        print(" ------- Gestão de Cinema ------- ")
        print("1. Inserir sala")
        print("2. Listar filmes em exibição")
        print("3. Verificar se um lugar está disponível")
        print("4. Vender bilhete")
        print("5. Listar disponibilidades por sala")
        print("6. Remover sala")
        print("0. Sair")
        print(" -------------------------------- ")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            filme = input("Insira o nome do filme: ")
            nlugares = int(input("Insira o valor correspondente ao número de lugares: "))
            nova_sala = (nlugares, [], filme)
            cinema = Inserir_Sala(cinema, nova_sala)

        elif opcao == "2":
            Listar(cinema)

        elif opcao == "3":
            filme = input("Insira o nome do filme: ")
            lugar = int(input("Insira o número do lugar: "))
            if Disponivel(cinema, filme, lugar):
                print(f"O lugar {lugar} está disponível para o filme '{filme}'.")
            else:
                print(f"O lugar {lugar} já está ocupado.")

        elif opcao == "4":
            filme = input("Insira o nome do filme: ")
            lugar = int(input("Insira o número do lugar: "))
            if Disponivel(cinema, filme, lugar):
                cinema = Vende_Bilhete(cinema, filme, lugar)
                print(f"Bilhete vendido para o lugar {lugar} no filme '{filme}'.")
            else:
                print(f"Não é possível vender o bilhete. O lugar {lugar} já está ocupado.")

        elif opcao == "5":
            Listar_Disponibilidades(cinema)

        elif opcao == "6":
            filme = input("Nome do filme a remover: ")
            cinema = Remover_Sala(cinema, filme)
            print(f"Sala do filme '{filme}' removida.")

        elif opcao == "0":
            print("Até à próxima!")

        else:
            print("Opção inválida. Tente novamente.")

Menu()


