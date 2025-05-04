# Variávies para em ordem crescente para utilizar no loop criando o rank de músicas top 3:
nome_musica1 = ''
nome_musica2 = ''
nome_musica3 = ''
qtd_streams1 = 0
qtd_streams2 = 0
qtd_streams3 = 0
# Loop para criar o rank de músicas top 3 da mais ouvida para a menos ouvida:
for i in range(3):
    nome_musica = input()
    qtd_streams = int(input())
    if (i == 0):
        nome_musica1, qtd_streams1 = nome_musica, qtd_streams
    elif (i == 1):
        if (qtd_streams >= qtd_streams1):
            nome_musica2, qtd_streams2 = nome_musica1, qtd_streams1
            nome_musica1, qtd_streams1 = nome_musica, qtd_streams
        else:
            nome_musica2, qtd_streams2 = nome_musica, qtd_streams
    elif (i == 2):
        if (qtd_streams >= qtd_streams1):
            nome_musica3, qtd_streams3 = nome_musica2, qtd_streams2
            nome_musica2, qtd_streams2 = nome_musica1, qtd_streams1
            nome_musica1, qtd_streams1 = nome_musica, qtd_streams
        elif (qtd_streams >= qtd_streams2):
            nome_musica3, qtd_streams3 = nome_musica2, qtd_streams2
            nome_musica2, qtd_streams2 = nome_musica, qtd_streams
        else:
            nome_musica3, qtd_streams3 = nome_musica, qtd_streams

# Print do top músicas em ordem crescente:
print(f'1º: {nome_musica1} teve {qtd_streams1} de streams e foi a música mais ouvida de Simone!')
print(f'2º: {nome_musica2} teve {qtd_streams2} de streams e foi a segunda música mais ouvida de Simone!')
print(f'3º: {nome_musica3} teve {qtd_streams3} de streams e completou o top 3 das músicas mais ouvidas da artista!')

# Como as variáveis musicas 1, musicas 2 e musicas 3 ja estão armazendas da maior ponutação para a menor.
# Basta fazer uma condicional para cada um e saber quem tem stream maior que 10 milhoes:
if(qtd_streams1 > 10000000):
    print(f'Uau! {nome_musica1} foi um hit certeiro da rainha do Natal!')
elif(qtd_streams1 < 1000000):
    print(f'Bom… a música {nome_musica1} não foi exatamente um sucesso nacional, mas foi o suficiente para entrar no topo da lista das mais ouvidas.')

if(qtd_streams2 > 10000000):
    print(f'Uau! {nome_musica2} foi um hit certeiro da rainha do Natal!')
elif(qtd_streams2 < 100000):
    print(f'Bom… a música {nome_musica2} não foi exatamente um sucesso nacional, mas foi o suficiente para entrar no topo da lista das mais ouvidas.')

if(qtd_streams3 > 10000000):
    print(f'Uau! {nome_musica3} foi um hit certeiro da rainha do Natal!')
elif(qtd_streams3 < 1000000):
    print(f'Bom… a música {nome_musica3} não foi exatamente um sucesso nacional, mas foi o suficiente para entrar no topo da lista das mais ouvidas.')

# Condicional para saber a diferença entre a música 1 (mais ouvida) e música 2 (2ª mais ouvida):
if(qtd_streams1 - qtd_streams2) > 5000000:
    print(f'{nome_musica1} foi disparada a mais ouvida neste ano! Nenhuma outra música natalina chega aos pés dela!')
elif(qtd_streams1 - qtd_streams2) < 1000000:
    print(f'{nome_musica1} foi a mais ouvida, mas não podemos esquecer da música {nome_musica2}! Fez bonito nesse feriado!')