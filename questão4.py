# Variavel para quantidade de folhas, populacao, altura da arvore, folhas e braille:
qtd_folhas = int(input())
populacao = int(input())
altura_arvore = int(input())
folhas_das_avores = 0
f = '+'
braille = '\u2800'

# Repeticao para calcular a quantidade de folhas
for i in range(altura_arvore, 1, -1):
    folhas_das_avores += i * 2

# Variavel para quantidade de arvores para populacao
arvore_para_populacao = folhas_das_avores * populacao

if(altura_arvore < 2):
    print('Isso não é uma árvore, é um arbusto!')
elif(qtd_folhas < folhas_das_avores):
    print('Infelizmente não poderemos comemorar o Natal esse ano, não conseguimos fazer uma única árvore!')
else:
    print(f'{braille * (altura_arvore + 1)}*')
    for k in range(1, altura_arvore + 1):
        print(f'{braille * (altura_arvore + 1 - k)}{f * k}', end='\u2800')
        print(f'{f * k}')
    if(arvore_para_populacao <= qtd_folhas):
        print('O Grinch não conseguiu estragar o Natal dessa vez!')
    else:
        print('Essa árvore está muito grande, dessa forma não conseguiremos entregar para a cidade toda')