i = int(input())  # 'i' para input().
braille = '\u2800'
e = '*'  # 'e' para estrela.

if i == 1:
    print('*')
else:
    print(f'{braille * (i - 1)}{e}{braille * (i - 1)}')
    # Triângulo superior.
    for superior in range(2, i, 1):
        print(f'{braille * (i - superior)}{e}', end=f'{braille}')
        print(f'{braille * ((2 * superior) - 4)}{e}{braille * (i - superior)}')
    print(f'{(e + braille) * (i - 1)}{e}')  # Divisão entre o triângulo superior e o inferior.
    # Triângulo inferior.
    for inferior in range(i - 1, 1, -1):  
        print(f'{braille * (i - inferior)}{e}', end=f'{braille}')
        print(f'{braille * ((2 * inferior) - 4)}{e}{braille * (i - inferior)}')
    print(f'{braille * (i - 1)}{e}{braille * (i - 1)}')  # Última estrela do triângulo inferior.
