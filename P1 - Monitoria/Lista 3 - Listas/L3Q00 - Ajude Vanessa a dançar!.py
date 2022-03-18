passos = []
passo = ''

while passo != "FIM":
    passo = input()
    if passo != "FIM":
        passos.append(passo)

print(f"Olá seguimores! O primeiro passo da dancinha é {passos[0]}")
print(f"Depois, a gente faz o {passos[1]} e {passos[2]}")
print(f"Temos ainda mais {len(passos) - 3} passos pra aprender!")
print(f"Por último, vamos fazer o {passos[-1]}")
