# Variáveis dos Presentes: Boneco, Videogame, Bicicleta e Outros inicando ambos com 0:
p1 = 0
p2 = 0
p3 = 0
outros = 0
presente = ''

# Laço de repetição:
while (presente != 'FIM'):
    presente = input()
    if(presente != 'FIM'):
        if(presente == 'Boneco' or presente == 'Videogame' or presente == 'Bicicleta'):
            print('Mais um presente saindo!')
            if(presente == 'Boneco'):
                p1+= 1
            elif(presente == 'Videogame'):
                p2+= 1
            elif(presente == 'Bicicleta'):
                p3+= 1
        else:
            outros += 1
            print('Esse presente não está sendo fabricado nesse momento')
    else:
        print('Vamos agora ao relatório dos presentes!\n')

# Calculo para quantidade total de presentes e suas respectivas quantidades percentuais:
qtd_presentes = p1 + p2 + p3 + outros
p1_porcentagem = (p1 * 100) / qtd_presentes
p2_porcentagem = (p2 * 100) / qtd_presentes
p3_porcentagem = (p3 * 100) / qtd_presentes
outros_porcentagem = (outros * 100) / qtd_presentes

# Print para os presentes, suas quatindades e quantidades percentuais:
print(f'Boneco - {p1} unidades - {p1_porcentagem:.2f}%')
print(f'Videogame - {p2} unidades - {p2_porcentagem:.2f}%')
print(f'Bicicleta - {p3} unidades - {p3_porcentagem:.2f}%')
print(f'Outros - {outros} unidades - {outros_porcentagem:.2f}%')

# Condicional para os outros presentes e as porcentagens:
if(outros == 0):
    print('A demanda está muito alta! Teremos que fazer mais uma fábrica!')
elif(outros_porcentagem > 50 ):
    print('Parece que o Papai Noel terá que fechar a fábrica :(')
elif(p1_porcentagem <= 50 and p2_porcentagem <= 50 and p3_porcentagem <= 50 and outros_porcentagem <= 50):
    print('A fábrica está cumprindo seu papel, porém não precisa ser expandida')
elif(p1_porcentagem > 50):
    print('Boneco está sendo muito desejado! A fábrica terá que ser expandida!')
elif(p2_porcentagem > 50):
    print('Videogame está sendo muito desejado! A fábrica terá que ser expandida!')
elif(p3_porcentagem > 50):
    print('Bicicleta está sendo muito desejado! A fábrica terá que ser expandida!')