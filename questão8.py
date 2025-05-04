# Entrad para a variável quantidade de rodadas:
qtd_rodadas = int(input())
meias_equipe_vencedora = 0 # Quantidade de meias para equipe vencedora.
equipe_vencedora = ''  # Equipe vencedora
meias_elfos = 0  # Quantidade de meias para equipe elfos.
meias_duendes = 0  # Quantidade de meias para equipe duendes.
print('O Torneio de Natal começa agora! Que vençam os melhores!')
# Loop para quantidade de rododadas:
for rodada in range(1, qtd_rodadas + 1):
    nome_equipe = input()
    desafio_equipe = input()
    dificuldade_desafio = input()
    qtd_meias = 0
    meias_por_rodadas = 0
    desafios_dificeis = 0
    print(f'RODADA {rodada}')
# Condicional para identificar o desafio da equipe e atribuir a pontuação de meias correspondente:
    if(desafio_equipe == 'Prepararam as roupas do Papai Noel.' or desafio_equipe == 'Alimentaram as renas.'):
        qtd_meias += 10
    elif(desafio_equipe == 'Arrumaram os estoques de doces.' or desafio_equipe == 'Guardaram os presentes no trenó.'):
        qtd_meias += 20
    elif(desafio_equipe == 'Ajudaram a carregar os presentes.' or desafio_equipe == 'Embrulharam os presentes.' or desafio_equipe == 'Decoraram a árvore de Natal.'):
        qtd_meias += 30
    elif(desafio_equipe == 'Planejaram a rota do Papai Noel.'):
        qtd_meias += 50
    elif(desafio_equipe == 'Testaram os brinquedos.'):
        qtd_brinquedos = int(input())
        qtd_meias = int((2 * qtd_brinquedos))
# Condicional para identificar a dificuldade do desafio da equipe e atribuir a pontuação de meias correspondente:
    if(dificuldade_desafio == 'Médio'):
        qtd_meias = int((qtd_meias + (qtd_meias * 0.2)))
    elif(dificuldade_desafio == 'Difícil'):
        qtd_meias = int((qtd_meias + (qtd_meias * 0.5)))
        desafios_dificeis += 1
# Condicional para identificar o evento surpresa da equipe e atribuir a pontuação de meias correspondente:
    evento_surpresa = input()
    if(evento_surpresa == 'Dia de Sorte'):
        qtd_meias += 30
        print('É um Dia de Sorte! Vocês ganharam 30 meias bônus!')
    elif(evento_surpresa == 'Dia de Azar'):
        qtd_meias -= 30
        print('É um Dia de Azar! Vocês perderam 30 meias!')
    elif(evento_surpresa == 'Grinch'):
        print('O Grinch está sabotando o Torneio!')
        mensagem_correta = f'{nome_equipe}, protejam as meias!'
        cor_meias = ''
        while (cor_meias != mensagem_correta):
            cor_meias = input()
            if(cor_meias == 'Amarelas'):
                qtd_meias -= 5
            elif(cor_meias == 'Verdes'):
                qtd_meias -= 10
            elif(cor_meias == 'Vermelhas'):
                qtd_meias -= 20
            else:
                mensagem_correta
    if(qtd_meias < 0): # Condicional para se a quantidade de meias for menor que zero.
        qtd_meias = 0
    meias_por_rodadas += qtd_meias
# Condicional para atribuir a equipe e quantidade de meias por rodadas:
    if(meias_por_rodadas > 0):
        print(f'A equipe dos {nome_equipe} ganhou {int(meias_por_rodadas)} meias nesta rodada.')
    else:
        print(f'Infelizmente, a equipe dos {nome_equipe} não ganhou meias nessa rodada.')
# Condicional para identificar a equipe e atribuir a pontuação de meias correspondente:
    if(nome_equipe == 'Elfos'):
        meias_elfos += meias_por_rodadas
    elif(nome_equipe == 'Duendes'):
        meias_duendes += meias_por_rodadas
# Condicional para identificar a equipe vencedora e a sua quantidade de meias:
if(meias_elfos > meias_duendes):
    equipe_vencedora = 'Elfos'
    meias_equipe_vencedora = meias_elfos
elif(meias_duendes > meias_elfos):
    equipe_vencedora = 'Duendes'
    meias_equipe_vencedora = meias_duendes
print('TORNEIO ENCERRADO!')
print('Segurem seus gorros que o Noel já vai entregar o Prêmio da Estrela Natalina.')
print(f'Os {equipe_vencedora} venceram o Torneio de Natal com um total de {int(meias_equipe_vencedora)} meias e terão a honra de ajudar o Papai Noel na noite mais mágica do ano.')