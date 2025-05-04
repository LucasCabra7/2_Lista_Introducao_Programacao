# Variáveis para quantidade de renas e quantidade de voltas:
qtd_renas = int(input())
qtd_voltas = int(input())

#Variáveis para o Top 3 do nome e pontuação final de cada rena:
nome_da_rena1, nome_da_rena2, nome_da_rena3 = '', '', ''
pontuacao_final_rena1, pontuacao_final_rena2, pontuacao_final_rena3 = 0, 0, 0

if(qtd_renas < 3): # Condicional para quantidade de renas ser menor que 3.
    print('Meu senhor, com essa quantidade de rena vai ter que entregar os presentes a pé, viu?!')
elif(qtd_renas == 3): # Condicional para quantidade de renas ser igual que 3.
    nome_da_rena1, nome_da_rena2, nome_da_rena3 = input(), input(), input()
    print(f'Como só temos 3 renas aptas pro serviço esse ano, não adianta muito querer ficar escolhendo')
    print(f'As três únicas renas capazes de participar esse ano são:')
    print(f'{nome_da_rena1}, {nome_da_rena2} e {nome_da_rena3}.')
    print('Não haverá teste de desempenho entre elas!')
elif(qtd_renas > 3): # Condicional para quantidade de renas ser maior que 3.
    for i in range(1, qtd_renas + 1): # Loop para incremetar a quantidade de nomes de renas, para a quantidade de renas desejadas.
        nome_da_rena = input()
        pontuacao_inicial_rena = 0
        pontuacao_final_rena = 0
        for letra in nome_da_rena.lower(): # Loop para pontuação de cada letra.
            if(letra == 'a'):
                pontuacao_inicial_rena += 8
            elif(letra == 'e'):
                pontuacao_inicial_rena += 5
            elif(letra == 'i'):
                pontuacao_inicial_rena += 4
            elif(letra == 'o'):
                pontuacao_inicial_rena += 3
            elif(letra == 'u'):
                pontuacao_inicial_rena += 2
        for j in range(1, qtd_voltas + 1): # Loop para pontuação dos restos.
            if(pontuacao_inicial_rena % j == 0): # Condicional se o resto da divisão deixa resto 0.
                pontuacao_final_rena += 2
            elif((pontuacao_inicial_rena % j) % 2 == 0): # Condicional se o resto da divisão deixa resto par.
                pontuacao_final_rena += 1
        pontuacao_final_rena += pontuacao_inicial_rena
        if(i == 1): # Condicional para classificação. 
            nome_da_rena1, pontuacao_final_rena1 = nome_da_rena, pontuacao_final_rena
        elif(i == 2): # Condicional para classificação top. 
            if(pontuacao_final_rena > pontuacao_final_rena1):
                nome_da_rena2, pontuacao_final_rena2 = nome_da_rena1, pontuacao_final_rena1
                nome_da_rena1, pontuacao_final_rena1 = nome_da_rena, pontuacao_final_rena
            elif(pontuacao_final_rena <= pontuacao_final_rena1):
                nome_da_rena2, pontuacao_final_rena2 = nome_da_rena, pontuacao_final_rena
        elif(i > 2): # Condicional para classificação top 3. 
            if(pontuacao_final_rena > pontuacao_final_rena1):
                nome_da_rena3, pontuacao_final_rena3 = nome_da_rena2, pontuacao_final_rena2
                nome_da_rena2, pontuacao_final_rena2 = nome_da_rena1, pontuacao_final_rena2
                nome_da_rena1, pontuacao_final_rena1 = nome_da_rena, pontuacao_final_rena
            elif(pontuacao_final_rena > pontuacao_final_rena2):
                nome_da_rena3, pontuacao_final_rena3 = nome_da_rena2, pontuacao_final_rena2
                nome_da_rena2, pontuacao_final_rena2 = nome_da_rena, pontuacao_final_rena
            elif(pontuacao_final_rena > pontuacao_final_rena3):
                nome_da_rena3, pontuacao_final_rena3 = nome_da_rena, pontuacao_final_rena
    print('As três renas mais atléticas pra temporada de Natal são:')
    print(f'{nome_da_rena1}, {nome_da_rena2} e {nome_da_rena3}.')