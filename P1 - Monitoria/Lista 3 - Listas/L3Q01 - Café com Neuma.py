meninos = []
meninas = []

n = int(input())
for i in range(n):
    nome, genero = input().split(' - ')
    if genero == "M":
        meninos.append(nome)
    elif genero == "F":
        meninas.append(nome)

if len(meninos) > 0:
    for i in range(len(meninos)):
        print(meninos[i], end=", ")
    print("Querem cafe?")
if len(meninas) > 0:
    for i in range(len(meninas)):
        print(meninas[i], end=", ")
    print("Desculpa, so pros meninos HAHAHAHAAHHAHAHA")

if len(meninos) > 0:
    print(f"Serao necessarias {len(meninos)} porcoes de cafe")
else:
    print("Nao tem meninos na lista, nao precisa fazer cafe, Neuma")
