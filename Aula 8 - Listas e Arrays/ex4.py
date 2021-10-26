# Fazer um programa Python para:
# – Ler uma seqüência de números inteiros positivos (ou
# zero).
# – A leitura deve parar com um número negativo.
# – O programa deve imprimir os números lidos cujos
# valores têm dois dígitos, mas na ordem inversa em
# que forem lidos – o último número lido deve ser o
# primeiro a ser impresso.

sequencia = []
contador = 0
indice = 0
while (contador >= 0):
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
