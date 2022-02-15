# Ler o nome completo do usuário e imprimi-lo com o
# primeiro e último nome escritos  em maiúsculas.

nome = input("Digite um nome completo: ")
nome = nome.strip()
while nome.find(" ") == -1:
    nome = input("ERRO!\nDigite um nome completo: ")
    nome = nome.strip()

esquerda = 0
while (esquerda < len(nome)) and (nome[esquerda] != ' '):
    esquerda += 1

direita = len(nome) - 1
while (direita >= 0) and (nome[direita] != ' '):
    direita -= 1

nome = nome[0:esquerda].upper() + nome[esquerda:direita] + nome[direita:].upper()
print(nome)
