n = int(input("Quantos alunos são? "))
while n < 0:
   print("Erro! O número de estudantes deve ser maior ou igual a 0.")
   n = int(input("Quantos alunos são? "))
v1 = [0] * n

somanotas = 0
for i in range(n):
    v1[i] = float(input(f"Digite a nota do {i+1}º aluno: "))
    somanotas += v1[i]
media = round((somanotas / n), 2)
print(f"Média da turma: {media}")

v1.sort(reverse=True)
contador = 0
for i in range(n):
    if v1[i] > media:
        contador += 1
print(f"Notas maiores que a média: {v1[:contador]}")
