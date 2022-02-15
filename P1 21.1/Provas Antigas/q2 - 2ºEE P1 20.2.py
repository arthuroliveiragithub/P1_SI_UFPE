# Q2 – Faça uma subrotina Python do tipo função recursiva para calcular a soma dos N primeiros
# termos da série abaixo, onde o valor de N é um parâmetro e o resultado do cálculo da série é o
# resultado da função.
# S = 105 / 25 – 130 / 35 + 140 / 45 – 160 / 55 + 175 / 65 – 190 / 75 ....
# OBS1 - Observe que você não pode usar os comandos de repetição nesta questão.
# OBS2 - Você pode (ou não) incluir um programa principal para testar a sua função: somente
# a função será avaliada na correção.

def soma_seq(n, num1=105, num2=-130, den=25, sinal=1):
    if sinal == 1:
        s = num1/den
    else:
        s = num2/den
    if n > 1:
        if sinal == 1:
            s = s + soma_seq(n-1, num1 + 35, num2, den + 10, -1)
        else:
            s = s + soma_seq(n-1, num1, num2 - 30, den + 10, 1)
    return s


n = int(input("Digite o número de termos da sequência: "))
while n <= 0:
    n = int(input("Digite um valor positivo.\nDigite o número de termos da sequência: "))
print(f"A soma dos {n} termos da sequência é {soma_seq(n):.2f}.")
