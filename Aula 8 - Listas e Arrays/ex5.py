# Altere o programa anterior para garantir que o
# usuário digitará no máximo 1000 números.

sequencia = []
contador = 0
indice = 0
while (contador >= 0) and (contador < 1000):
    sequencia.append(int(input(f"Digite o {indice + 1}º elemento da sequência: ")))
    if (sequencia[indice] >= 0):
        contador += 1
        indice += 1
    else:
        contador = -1

saida = []
for i in range(indice):
    if (sequencia[i] > 9) and (sequencia[i] <= 99):
        saida.append(sequencia[i])

print(saida[::-1])
