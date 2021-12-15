# Q1 – A média ponderada de N números é a soma dos produtos de cada um deles multiplicados
# por seus respectivos pesos; o resultado dessa soma é então dividido pela soma dos pesos. A
# média ponderada é utilizada em diversas disciplinas para calcular os resultados dos alunos
# considerando duas avaliações parciais com pesos variáveis. As regras para definição do
# resultado são as seguintes:
#  Se a média do aluno for maior ou igual a sete, o aluno “está aprovado”.
#  Se a média do aluno for menor que três, o aluno “está reprovado”.
#  Se a média do aluno for menor que sete e maior ou igual a três, ele “fará prova final”.
# Faça uma subrotina Python do tipo procedimento que (a) receba o nome de um único aluno
# como parâmetro, (b) leia as notas das duas avaliações parciais desse aluno, (c) calcule sua média,
# e (d) imprima seu resultado como: "O aluno __________ obteve média ____ e __________."
# OBS - Os pesos utilizados no procedimento (peso1 e peso2) são parâmetros opcionalmente
# recebidos na chamada e, se não forem informados, seus valores devem ser 1.
# OBS2 - Você pode (ou não) incluir um programa principal para testar a sua subrotina: somente a
# função será avaliada na correção.

def calcula_media(aluno):
    n = 2
    peso = [0] * n
    nota = [0] * n
    soma_peso = media = 0
    for i in range(n):
        peso[i] = int(input(f'Digite o peso da nota da {i+1}ª avaliação de {aluno}: '))
        while peso[i] <= 0:
            print('Digite um valor acima de 0.')
        nota[i] = float(input(f'Digite a {i+1}ª nota de {aluno}: '))
        while nota[i] > 10 or nota[i] < 0:
            print('Digite um valor entre 0 e 10.')
            nota[i] = float(input(f'Digite a {i + 1}ª nota de {aluno}: '))
        media += (peso[i] * nota[i])
        soma_peso += peso[i]
    media /= soma_peso
    if media >= 7:
        print(f'O aluno {aluno} obteve média {media:.2f} e está aprovado.')
    elif media < 3:
        print(f'O aluno {aluno} obteve média {media:.2f} e está reprovado.')
    else:
        print(f'O aluno {aluno} obteve média {media:.2f} e fará prova final.')


aluno = "Maria"
calcula_media(aluno)
