# Questão 2 - 1º EE P1  21.1

qtd = 0
sequencia = [0]*400
negativos = [0]*400
positivos = [0]*400
soma = 0
qtd3pos = 0
qtd3neg = 0

num = int(input("Digite um número inteiro: "))
while num != -9999999999 and qtd < 400:
    sequencia[qtd] = num
    qtd += 1
    if (num > 99) and (num < 1000):
        positivos[qtd3pos] = num
        qtd3pos += 1
        soma += num
    elif (num > -1000) and (num < -99):
        negativos[qtd3neg] = num
        qtd3neg += 1
        soma += num

    num = int(input("Digite mais um número inteiro ou -9999999999 para parar: "))

if qtd == 400:
    print("Quantidade máxima de números atingida.")
if qtd < 400:
    print(f"A quantidade de números inteiros lidos foi: {qtd - 1}")
else:
    print(f"A quantidade de números inteiros lidos foi {qtd}")

if qtd3pos == 0 and qtd3neg == 0:
    print("Não foram encontrados números com 3 algarismos significativos")
else:
    print(f"Os números lidos com 3 algarismos significativos foram:\n{negativos[:qtd3neg]}\n{positivos[:qtd3pos]}")
    media = soma / (qtd3neg + qtd3pos)
    print(f"A média dos números de 3 dígitos foi igual a {media:.2f}")
