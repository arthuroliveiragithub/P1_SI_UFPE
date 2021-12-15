# Q1 – Escreva uma subrotina Python do tipo função recursiva chamada CalculaS para calcular a
# soma dos N primeiros termos da série abaixo, onde o valor de N é um parâmetro e o resultado
# do cálculo da série é o resultado da função.
# S = 1 / 2 – 3 / 4 + 9 / 4 – 27 / 9 + 81 / 8 – 243 / 14 + ...
# OBS - Observe que você não pode usar os comandos de repetição nesta função.
# Escreva também uma subrotina Python do tipo procedimento chamada Imprime que
# deve receber como parâmetro uma lista contendo números inteiros e, para cada um dos
# elementos da lista, na ordem em que estiverem na lista, deve usar a função CalculaS, e depois
# imprimir o resultado da função (com 3 casas decimais), da seguinte forma:
# “O resultado de S com ... termos é ...”.
# Escreva ainda um programa principal para repetidamente perguntar ao usuário o número
# de termos desejados até que o usuário digite um número de termos inválido. Depois, o seu
# programa deve (a) imprimir a quantidade de cálculos que o usuário solicitou e, em seguida,
# (b) usar o procedimento Imprime para imprimir todos os resultados solicitados pelo usuário
# em ordem decrescente do número de termos.


def CalculaS(n, num1=1, num2=-3, den1=2, den2=4, sinal=1):
    if sinal == 1:
        s = num1/den1
    else:
        s = num2/den2
    if n > 1:
        if sinal == 1:
            s = s + CalculaS(n-1, num1*9, num2, den1*2, den2, -1)
        else:
            s = s + CalculaS(n-1, num1, num2*9, den1, den2+5, 1)
    return s


def Imprime(lista, contador):
    lista.sort(reverse=True)
    for i in range(contador):
        print(f'O resultado de S com {lista[i]} termos é {CalculaS(lista[i]):.3f}')


lista = [0]
contador = 0
n = int(input("Digite o número de termos da sequência: "))
while n > 0:
    lista.append(n)
    contador += 1
    n = int(input("Digite o número de termos da sequência: "))
Imprime(lista, contador)
