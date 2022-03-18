lista_tiktokers = []

n_tiktokers = int(input())
for i in range(n_tiktokers):
    nome_seguidores = input().split("-")
    lista_tiktokers.append(nome_seguidores)

for i in range(len(lista_tiktokers)):
    for j in range(len(lista_tiktokers) - 1):
        if int(lista_tiktokers[j][1]) > int(lista_tiktokers[j+1][1]):
            lista_tiktokers[j], lista_tiktokers[j + 1] = lista_tiktokers[j+1], lista_tiktokers[j]
        elif int(lista_tiktokers[j][1]) == int(lista_tiktokers[j+1][1]) and len(lista_tiktokers[j][0]) < len(lista_tiktokers[j+1][0]):
            lista_tiktokers[j], lista_tiktokers[j + 1] = lista_tiktokers[j+1], lista_tiktokers[j]

for elemento in lista_tiktokers:
    print("-".join(elemento))
