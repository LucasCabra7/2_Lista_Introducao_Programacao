print('Bem-vindo à missão dos duendes! Vamos construir o trenó mágico do Papai Noel!') # primeiro enigma
print('Quantos materiais mágicos estão trancados nos baús?')
print('Vamos começar desbloqueando os materiais!')
qtd_materiais = int(input())
itens_desbloqueados = int(0)
for a in range(1, qtd_materiais + 1, 1): # entrada dos materiais para o jogo da forca  
    print(f'Material {a} de {qtd_materiais}')
    nome_item, letras_certas, n_vezes = input(), int(0), int(0) # variáveis
    nome_crip = nome_item
    letra_chutadas = ''
    for z in f'{nome_crip}': # cripitografia da palavra mantendo apenas os espaços
        if z != ' ':
            nome_crip = nome_crip.replace(z,'_')
    print(f'Senha mágica: {nome_crip}')
    if len(nome_item) <= 5: # decidindo o número de chance para acerta a senha mágica 
        numeros_de_chutes = 7
    elif len(nome_item) <= 10:
        numeros_de_chutes = 9
    elif len(nome_item) <= 13:
        numeros_de_chutes = 13
    else:
        numeros_de_chutes = 16
    for b in range(1, numeros_de_chutes + 1, 1): # jogo da forca 
        if  letras_certas < len(nome_item.replace(' ', '')): # garantia de que se ele acerta antes de as chances acabar não peça outro input 
            letra = input()
            if ((letra not in nome_item) or (letra in letra_chutadas)) and b == numeros_de_chutes : # ultima tentativa errada
                print('Infelizmente não conseguimos descobrir a senha.')
            elif letra not in nome_item: # tentativa errada
                print(f'Erramos a letra! Porém ainda temos mais tentativas.')
            elif letra not in letra_chutadas: # acertou!! e não repetiu 
                for r in nome_item : # quantas vezes a letra chutada apacerce na palavra 
                    if r == letra:
                        n_vezes += 1
                letras_certas += n_vezes
                if n_vezes == 1:
                    print('Acertamos uma letra! Ela aparece um total de 1 vez na senha')
                    n_vezes = 0
                else:
                    print(f'Acertamos uma letra! Ela aparece um total de {n_vezes} vezes na senha')
                    n_vezes = 0
            letra_chutadas += letra
    if letras_certas == len(nome_item.replace(' ','')): # vericação se acertou ou não a palavra 
        print(f"Parabéns! Você desbloqueou o material mágico '{nome_item}'!")
        itens_desbloqueados += 1
    else:
        print(f"Você não conseguiu desbloquear o material. O nome correto era '{nome_item}'.")
print(f'Você desbloqueou {itens_desbloqueados} de {qtd_materiais} materiais mágicos!') # fim primeiro enigma !!
print('Os duendes precisam decifrar os códigos perdidos para montar o trenó!') # segundo enigma 
print('Quantas partes o trenó possui?')
qtd_partes = int(input())
partes_montadas = int(0)
for parte in range(1, qtd_partes + 1, 1): 
    print(f'Parte {parte} de {qtd_partes}')
    sequecia = input() # entrada do código mágico 
    sequecia = sequecia + ' '
    maior, menor, numero = '', '', ''
    for n in sequecia: # lendo os número sequencia
        if n != ' ':
            numero = numero + n
        else: # achando o maior e o menor número 
            if maior == '' and menor == '':
                menor, maior = int(numero), int(numero)
            elif int(numero) > maior:
                maior = int(numero)
            elif int(numero) < menor:
                menor = int(numero)
            numero = '' 
    numero_magico = maior + menor
    print(f'Dica: O menor número é {menor} e o maior número é {maior}.')
    print(f'Descubra o número mágico (soma de {menor} e {maior})')
    tentativa_certa = int(0)
    for chances in range(2): # tentativa de acerta o número mágico
        if tentativa_certa == 0: # garantia de que se ele acerta na primeira vez não peça outro input 
            tentativa = input()
            if int(tentativa) == numero_magico : # acertou!!
                print(f'Você decifrou o código da parte {parte}! O trenó está mais próximo de ficar completo!')
                partes_montadas += 1
                tentativa_certa += 1
            elif chances == 0: # primeira chance errada 
                print(f'Número incorreto! Tente novamente.')
                print(f'Descubra o número mágico (soma de {menor} e {maior})')
            elif chances == 1: # segunda chance errada 
                print(f'Número incorreto! Tente novamente.')
                print(f'Você não conseguiu decifrar o código. O número mágico era {numero_magico}.')
print(f'Você montou {partes_montadas} de {qtd_partes} partes do trenó!')
if partes_montadas == qtd_partes: # final!!
    print('Parabéns! O trenó está completo e pronto para voar!')
elif partes_montadas >= (qtd_partes //2):
    print('Bom trabalho! O trenó quase ficou completo!')
else:
    print('Parece que o trenó ficou incompleto. Tente novamente na próxima missão!')
