# Variáveis musica, quantidade de musicas da playlist, ultima musica adicionada e a quantidade de ataque dos vilões:
musica = ''
qtd_musica = 0
ultima_musica = ''
ataque_viloes = 0

print('PLAYLIST DO PAPAI NOEL')

# Estrutura de laços:
while musica != 'FIM':
    musica = input()
    musica_sem_espacos = musica.replace(' ', '')
    if(musica.isnumeric()):
        ataque_viloes += 1
        if(ataque_viloes == 3):
            print('NAAÃO! Já está na hora do Papai Noel sair e não conseguimos construir sua playlist perfeita.')
            musica = 'FIM'
        else:
            print('ABORTAR! OS VILÕES OBTIVERAM ACESSO, TEREMOS QUE RECOMEÇAR.')
            print('PLAYLIST DO PAPAI NOEL')
            qtd_musica = 0
            ultima_musica = ''
    elif(musica_sem_espacos.isalpha()) and (len(musica_sem_espacos) >= 15):
        print(f'{musica} foi adicionada à playlist!')
        qtd_musica += 1
        ultima_musica = musica
    elif(musica == 'FIM'):
        if(qtd_musica == 0):
            print(f'Infelizmente não conseguimos encontrar nenhuma música para a playlist do Papai Noel...')
        else:
            print(f'Ufa! Conseguimos criar a playlist perfeita, tomara que o Papai Noel goste das {qtd_musica} músicas.')
    else:
        if(qtd_musica != 0):
            print(f'{musica} não pôde ser adicionada à playlist! A última música adicionada foi {ultima_musica}.')
        else:
            print(f'{musica} não pôde ser adicionada e a playlist continua vazia. Papai Noel precisa da sua ajuda!')