n_competidores = int(input())
contador = 0
quantidade_vencedor = 0
vencedor = ''

while contador < n_competidores:
    competidor = input()
    quantidade_latinhas = int(input())
    if quantidade_latinhas > quantidade_vencedor:
        quantidade_vencedor = quantidade_latinhas
        vencedor = competidor
    contador += 1

print(f'{vencedor} e o novo anjo!')
