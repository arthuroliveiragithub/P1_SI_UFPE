# Questão 1 - 1º EE P1  21.1

n = int(input("Digite o valor de N, que deve ser positivo: "))
while n < 1:
    n = int(input("N deve ser positivo! Digite um valor válido: "))

num1 = 10
den1 = 1
num2 = 12
den2 = 5
soma = 0.0

for i in range(n):
    if i % 2 == 0:
        soma = soma + num1 / den1
        num1 = num1 + 4
        den1 = den1 + 7
    else:
        soma = soma - num2 / den2
        num2 = num2 + 4
        den2 = den2 + 6

print(f"A soma com {n} termos é igual a {soma:.2f}")
