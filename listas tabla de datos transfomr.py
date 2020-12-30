

data = [":Transformers#Est_1:24&Estrellas_2:45&Estrellas_3:13&",
        ":Capitana Marvel#Est_2:54&Estrella_3:321&Estrels_1:130&",
        ":Aquaman#Est_1:231&Estres_2:55&Estrs_3:23&",
        ":Capitán América#Est_1:243&Estres_3:155&Estres_2:38&",
        ":Los Minions#Estrella_2:541&Estrella_1:55&Estrellas_3:178&",
        ":Iron Man 3#est_1:440&estrellas_2:123&Etrellas_3:150&",
        ":Star Wars#Est_3:124&Estres_2:78&Estrs_1:62&"]




def extrae_pos_campos_xcadpersona(stringCadenaPorpersona):
    ini_fin =[] # lista q almacena posiciones
   # print(stringCadenaPorpersona)
    for i in range(len(stringCadenaPorpersona)):
        if stringCadenaPorpersona[i] ==":":
            ini_fin.append(i+1)

        elif stringCadenaPorpersona[i] == "#":
            ini_fin.append(i-1)

        elif stringCadenaPorpersona[i] == "&":
            ini_fin.append(i-1)
    ini_fin.append(i)
    return ini_fin

def extrae_campo(stringCadenaPorpersona, lisPosCampXpersona):
    data =[]
    for i in range(0, len(lisPosCampXpersona)-1, 2):
        data.append(stringCadenaPorpersona[lisPosCampXpersona[i]:lisPosCampXpersona[i+1]+1])
    return data

def calcula_estrella(numeroestrellas):
    est1 = int(numeroestrellas[0])
    est2 = int(numeroestrellas[1])
    est3 = int(numeroestrellas[2])


    if est1 > est2  and est1 > est3 :
        return 1
    elif est2 > est1  and est2 >est3 :
        return 2
    else:
        return 3


def reorganizar_datos(data):
    salida =[]
    for stringCadenaPorpersona in data:# stringCadenaPorpersona es un elemento de la lista
        lisPosCampXpersona = extrae_pos_campos_xcadpersona(stringCadenaPorpersona)
        registro = extrae_campo(stringCadenaPorpersona, lisPosCampXpersona)
        registro.append(calcula_estrella(registro[1:4]))
       # print(lisPosCampXpersona)
       # print(registro)
        salida.append(registro)
    return salida

def print_data(data):
    print("Titulo Pel.", "\t\tEst 1", "\tEst 2", "\tEst 3", "\tMaximo")
    for i in data:
        for j in i:
            print(j, end="\t\t")
        print()


print_data(reorganizar_datos(data))

