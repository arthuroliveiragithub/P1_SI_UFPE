# 4. Ler o nome completo do usuário e imprimi-lo com o
# primeiro e último nome escritos td em maiúsculas.

nome = input("Digite seu nome completo: ")
nome = nome.strip()
while nome.find(" ") == -1:
    nome = input("ERRO!\nDigite seu nome completo: ")
    nome = nome.strip()

nome = nome.split()
nome[0] = nome[0].upper()
nome[-1] = nome[-1].upper()
nome = " ".join(nome)

print(nome)
