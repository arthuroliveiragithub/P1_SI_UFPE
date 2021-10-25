x1 = float(input('Pense em três números. Digite o primeiro deles:'))
x2 = float(input('Digite o segundo número: '))
x3 = float(input('Digite o terceiro número: '))
menor = x1

if menor >= x2:
    menor = x2
elif menor >= x3:
    menor = x3

print(f'O menor dos valores digitados foi {menor}.')
