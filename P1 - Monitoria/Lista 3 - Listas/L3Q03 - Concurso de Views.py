participantes = []

for i in range(3):
    nome = input()
    qtd_views_1 = int(input())
    qtd_views_2 = int(input())
    media = int((qtd_views_1 + qtd_views_2) / 2 )
    participantes.append([nome, media])

for j in range(len(participantes) - 1):
    for i in range(len(participantes) - 1):
        if participantes[i][1] < participantes[i+1][1]:
            participantes[i], participantes[i+1] = participantes[i+1], participantes[i]

for i in range(len(participantes)):
    output = f"{i+1}º Lugar: {participantes[i][0]} com a media de views: {participantes[i][1]}"
    print(output)
