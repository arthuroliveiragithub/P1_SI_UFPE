lista_bruxos, lista_maior_poder, lista_menor_poder = [], [], []

num_bruxos = int(input())
for i in range(num_bruxos):
    bruxo = input().split()
    nome = bruxo[0]
    poder = int(bruxo[1])
    lista_bruxos.append([nome, poder])

maior_poder = lista_bruxos[0][1]
menor_poder = lista_bruxos[0][1]

for bruxo in lista_bruxos:
    if bruxo[1] > maior_poder:
        maior_poder = bruxo[1]
    elif bruxo[1] < menor_poder:
        menor_poder = bruxo[1]

for idx in range(len(lista_bruxos)):
    if lista_bruxos[idx][1] == maior_poder:
        lista_maior_poder.append(lista_bruxos[idx][0])
    elif lista_bruxos[idx][1] == menor_poder:
        lista_menor_poder.append(lista_bruxos[idx][0])

maiores_poderes = ", ".join(lista_maior_poder)
menores_poderes = ", ".join(lista_menor_poder)

print(f"Sr Dumbledore, o maior poder de magia foi {maior_poder}, "
      f"e a nova força será composta pelo(s) seguinte(s) aluno(s): {maiores_poderes}. "
      f"Infelizmente, o menor nível de poder foi {menor_poder} "
      f"e os aluno(s) expulso(s): {menores_poderes}.")
