import matplotlib.pyplot as plt

# Definir o Menu
def Menu():
    print(" ------------------------------------ MENU ------------------------------------ ")
    print("1. Calcular Temp. média de cada dia")
    print("2. Guardar tabela meteorológica num ficheiro de texto")
    print("3. Carregar tabela meteorológica de um ficheiro de texto")
    print("4. Calcular Temp.mín. mais baixa da tabela")
    print("5. Calcular amplitude térmica de cada dia")
    print("6. Calcular o dia da precipitação máx.")
    print("7. Calcular o nº de dias em que a precipitação é maior que um valor p")
    print("8. Calcular maior nº de dias consecutivos com precipitação abaixo do limite p")
    print("9. Desenhar gráficos da Temp.mín., Temp.máx. e pluviosidade")
    print("0. Sair")
    print(" ------------------------------------------------------------------------------ ")


# Definir as Funções
def Medias(tabMeteo):
    res = []
    for x in tabMeteo:
        TempMedia = (x[1] + x[2])/2
        Data = x[0]
        res.append ((Data,TempMedia))
    return res

def Guardar_TabMeteo(t, fnome):
    file = open(fnome,"w")

    for data, min, max, prec in t:
        ano, mes, dia = data
        registo =f"{ano}-{mes}-{dia} | {min} | {max} | {prec}\n"
        file.write(registo)
    file.close()
    return

def Carregar_TabMeteo(fnome):
    res = []
    file = open(fnome, "r")
    for line in file:
        line = line.strip() # (ou line = line[:-1]) # strip remove espaços,\n,...
        campos = line.split("|")
        data, min, max, prec = campos
        ano, mes, dia = data.split("-")
        tuplo = ((int(ano), int(mes), int(dia)), float(min), float(max), float(prec))
        res.append(tuplo)
    file.close()
    return res

def Temp_Min(tabMeteo):
    minimo = tabMeteo[0][1]
    for data, min, *_ in tabMeteo:
        if min < minimo:
            minimo = min
    return minimo

def Ampl_Term(tabMeteo):
    res = []
    for elem in tabMeteo:
        ampl = (elem[2] - elem[1])
        data = elem[0]
        res.append((data, ampl))
    return res

def Max_Chuva(tabMeteo):
    data_max = None
    valor_max = 0
    for data, Tmin, Tmax, prec in tabMeteo:
        if prec > valor_max:
            data_max = data
            valor_max = prec
    return(data_max, valor_max)

def Dias_Chuvosos(tabMeteo, p):
    res = []
    for data, min, max, prec in tabMeteo:
        if prec > p:
            res.append((data, prec))
    return res

def Max_PeriodoCalor(tabMeteo, p):
    dias = 0
    maior = 0
    for data, min, max, prec in tabMeteo:
        if prec < p:
            dias = dias + 1
        else:
            if dias > maior:
                maior = dias 
            dias = 0

    if dias > maior:
        maior = dias

    return maior


def Graf_TabMeteo(t):
    #datas = [f"{ano}-{mes}-{dia}" for (ano, mes, dia), *_ in t]
    datas = [f"{data[0]}-{data[1]}-{data[2]}" for data, *_ in t]
    temps_min = [min for data, min, *_ in t]
    temps_max = [max for data, min, max, prec in t]
    precs = [prec for data, min, max, prec in t]

    plt.plot(datas,temps_min, label = "Temperatura Mínima", color = "c", marker = "o")
    plt.plot(datas,temps_max, label = "Temperatura Máxima", color = "green", marker = "o")
    plt.xlabel("Data")
    plt.ylabel("Temperatura, ºC")
    plt.title("Temperatura Mínima")
    plt.legend()
    plt.show()

    plt.bar(datas,precs, label = "Precipitação", color = "pink")
    plt.xlabel("Data")
    plt.ylabel("Precipitação, mm")
    plt.title("Precipitação")
    plt.legend()
    plt.show()


    return


# Definir o Main
def Main():
    tabMeteo =[]
    fnome = "meteorologia.txt"
    p = None

    while True:
        Menu()
        opcao = input("Introduza uma opção: ")

        if opcao == "1":
            resultado = Medias(tabMeteo)
            print(f"Temperaturas médias de cada dia: {resultado}")

        elif opcao == "2":
            Guardar_TabMeteo(t, fnome)
            print(f"Tabela guardada em {fnome}")

        elif opcao == "3":
            tabMeteo = Carregar_TabMeteo(fnome)
            print(f"Tabela carregada: {tabMeteo}")

        elif opcao == "4":
            resultado = Temp_Min(tabMeteo)
            print(f"Temperatura mínima mais baixa: {resultado}")

        elif opcao == "5":
            resultado = Ampl_Term(tabMeteo)
            print(f"Amplitude térmica de cada dia: {resultado}")

        elif opcao == "6":
            resultado = Max_Chuva(tabMeteo)
            print(f"Dia de precipitação máxima: {resultado}")
        
        elif opcao == "7":
            p = float(input("Introduza um valor para o limite p:"))
            resultado = Dias_Chuvosos(tabMeteo, p)
            print(f"Dias com precipitação maior que {p}: {resultado}")
        
        elif opcao == "8":
            p = float(input("Introduza um valor para o limite p:"))
            resultado = Max_PeriodoCalor(tabMeteo, p)
            print(f"Número máximo de dias consecutivos com precipitação abaixo de {p}: {resultado}")

        elif opcao == "9":
            if tabMeteo:
                Graf_TabMeteo(tabMeteo)
            else:
                print("Insira na tabela os dados necessários para a criação dos gráficos.")
        
        elif opcao == "0":
            print("Até à próxima!")
            return

tabMeteo = [((2022,1,20), 2, 16, 0),((2022,1,21), 1, 13, 0.2), ((2022,1,22), 7, 17, 0.01)]  
        
Main()