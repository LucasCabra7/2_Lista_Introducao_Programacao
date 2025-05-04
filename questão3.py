# Variáveis para continuidade da entrega de presentes, velocidade do papai noel em KM e M, quantidade de presentes e tempo total, respectivamente:
i = ''
velocidade_noel_km = 80
velocidade_noel_m = 80 * 1000
qtd_presentes = 0
tempo_total = 0

# Print inicial, antes do loop.
print('Boa noite, Papai Noel! Feliz Natal!')

# Código do loop:
while (i != 'FIM'):
    i = input()
    if(i == 'As renas ainda estão cheias de energia para entregar presentes para mais crianças!'):
        nome_da_crianca = input()
        distancia = float(input())
        unidade_de_medida = input()
        if(unidade_de_medida == 'quilometros'):
            tempo_min = ((distancia / velocidade_noel_km) * 60)
            if(tempo_min >= 60):
                print(f'Querido Papai Noel, você levará {int(tempo_min / 60)} horas para chegar até a casa de {nome_da_crianca}!')
                qtd_presentes += 1
                tempo_total += tempo_min
            elif(tempo_min >= 1 and tempo_min < 60):
                print(f'Querido Papai Noel, você levará {int(tempo_min)} minutos para chegar até a casa de {nome_da_crianca}!')
                qtd_presentes += 1
                tempo_total += tempo_min
            elif(tempo_min < 1):
                print(f'Querido Papai Noel, você chegará em breve na casa de {nome_da_crianca}!')
                qtd_presentes += 1
                tempo_total += tempo_min
        elif(unidade_de_medida == 'metros'):
                tempo_min = ((distancia /velocidade_noel_m ) * 60)
                if(tempo_min >= 60):
                    print(f'Querido Papai Noel, você levará {int(tempo_min / 60)} horas para chegar até a casa de {nome_da_crianca}!')
                    qtd_presentes += 1
                    tempo_total += tempo_min
                elif(tempo_min >= 1 and tempo_min < 60):
                    print(f'Querido Papai Noel, você levará {int(tempo_min)} minutos para chegar até a casa de {nome_da_crianca}!')
                    qtd_presentes += 1
                    tempo_total += tempo_min
                elif(tempo_min < 1):
                    print(f'Querido Papai Noel, você chegará em breve na casa de {nome_da_crianca}!')
                    qtd_presentes += 1
                    tempo_total += tempo_min
    else:
        i = 'FIM'

# Print após todas as visitas e entrega de presentes informando o tempo total gasto e a quantidade de presentes:
print(f'Querido Papai Noel, a noite de natal foi um sucesso! Você levou apenas {tempo_total / 60:.2f} horas para entregar todos os {qtd_presentes} presentes')