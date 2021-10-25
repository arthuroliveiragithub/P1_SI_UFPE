import math

x = int(input("Digite um número inteiro: "))
y = int(input("Digite mais um número inteiro: "))

while(y == 0):
    y = int(input("Segundo número tem que ser diferente de zero. Digite um número válido: "))

if x % y == 0:
    print(f'O resto da divisão entre os números é zero. O primeiro número foi {x}.')
else:
    res = math.pow(x%y,2)
    print(f'O resto da divisão foi diferente de zero e seu quadrado é igual a {res}.')
