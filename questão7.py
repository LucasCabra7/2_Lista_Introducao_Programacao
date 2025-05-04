# Variáveis para entrada da quantidade de membros:
qtd_membros = int(input())

# Variável para nome do filme, nacionalidade, quantidade de filmes brasileiros, estrangeiros e soma das notas.
nome_filme = ''
nacionalidade_filme = ''
n_filmes_brasileiros = 0
n_filmes_estrangeiros = 0
soma_das_notas = 0
# Apresentação inicial:
print('MARATONA DE NATAL: PAVÊ, RABANADA E FILMES')
# Loop para funcionalidade do código com a condição do nome do filme:
while (nome_filme != 'chega de filmes por hoje'):
    nome_filme = input()
    if(nome_filme != 'chega de filmes por hoje'):
        nacionalidade_filme = input()
        if(('natal' in nome_filme.lower() or 'magia' in nome_filme.lower() or 'papai noel' in nome_filme.lower()) and (nacionalidade_filme.lower() == 'brasil' or nacionalidade_filme.lower() == 'br')):
            n_filmes_brasileiros += 1
            for i in range(1, qtd_membros + 1): # Loop para o pedido de notas pela quantidade de membros.
                nota = int(input())
                soma_das_notas += nota
            media = (soma_das_notas / qtd_membros)
            print(f'{n_filmes_brasileiros}º filme: {nome_filme}')
            print(f'Média de votos para \'{nome_filme}\': {media:.1f}')
            soma_das_notas = 0
        elif('natal' in nome_filme.lower() or 'magia' in nome_filme.lower() or 'papai noel' in nome_filme.lower()):
            n_filmes_estrangeiros += 1     
# Condicional para o nª de filmes brasileiros:
print(f'{n_filmes_brasileiros} Filmes BR X {n_filmes_estrangeiros} Filmes FORA')
if(n_filmes_brasileiros == 0):
    print('Infelizmente esse ano não será nem pa vê e nem pa comer, sua lista não possui um filme bom, ops… nacional')
elif(n_filmes_brasileiros == 1):
    print('De toda sua lista, apenas UM filme de natal é nacional, melhore suas escolhas e tente novamente!')
elif(n_filmes_brasileiros > 1):
    print('A ceia está servida? Porque aqui estão os filmes brasileiros que vão dar o toque especial da sua maratona no Natal!')