# 4. Ler o nome completo do usuário e imprimi-lo com o
# primeiro e último nome escritos td em maiúsculas.

nome = input("Digite seu nome completo: ")
nome = nome.strip()
while nome.find(" ") == -1:
    nome = input("ERRO!\nDigite seu nome completo: ")
    nome = nome.strip()

esquerda = nome.find(' ')
direita = nome.rfind(' ')
nome = nome[:esquerda].upper() + nome[esquerda:direita] + nome[direita:].upper()

print(nome)
