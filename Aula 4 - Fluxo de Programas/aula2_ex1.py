import math

x = int(input("Digite um número inteiro: "))

if x % 2 == 0:
    res = math.pow(x,2)
    print(f"O quadrado de x é {res}")
else:
    res = x * 5
    print(f'5 vezes x é igual a {res}.')
