#Faça um programa para ler o arquivo "titanic.txt" e armazenar
# o nome, o sexo e a idade de todos os passageiros sobreviventes
# em "sobreviventes.txt".
# Ao final do programa imprima na tela:
# 1) a quantidade de sobreviventes homens;
# 2) a quantidade de sobreviventes mulheres; e
# 3) a média de idade de todos os sobreviventes.

try:
    leitura = open('titanic.txt', 'r')
    escrita = open('sobreviventes.txt', 'w')

    tot_male_surv = tot_female_surv = media_age_surv = 0
    with leitura, escrita:
        escrita.write("Name,Sex,Age\n")
        for linha in leitura:
            passengerId, survived, p_class, name, sex, age, sib_sp, parch, ticket, fare, cabin, embarked = linha.split(',')
            if survived == '1':
                escrita.write(f'{name},{sex},{age}\n')
                media_age_surv += float(age)
                if sex == 'male':
                    tot_male_surv += 1
                else:
                    tot_female_surv += 1
        media_age_surv = media_age_surv/(tot_male_surv + tot_female_surv)

except FileNotFoundError as msg:
    print(msg)
except PermissionError:
    print("Sem permissão de escrita.")
else:
    print(f'1) Sobreviventes homens: {tot_male_surv}')
    print(f'2) Sobreviventes mulheres: {tot_female_surv}')
    print(f'3) Média de idade dos sobreviventes: {media_age_surv:.2f}')