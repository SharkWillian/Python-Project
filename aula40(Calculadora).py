"""
Calculadora com while
"""
while True: #While começa sem dependencia de algo
    print('Bem vindo a merda da calculadora pistola')
    num_1 = input('Digite um número aí! ')
    num_2 = input('MANDA MAIS UM! ')
    operador = input('O que vc quer fazer com essas merdas? Digite um operador ')

    num_validos = None 

    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        num_validos = True
    
    except:
        num_validos = None

    if num_validos is None:
        print('Digite dois números válidos, porra')
        continue

    operadores_permitidos = '-+*/'
    
    if operador not in operadores_permitidos:
        print('Digita um operador de gente normal, porra ')
        continue

    if len(operador) > 1:
        print('Digita UM operador, não sabe ler? ')
        continue

    print('Tô calculando ssaporra')
    if operador == '+':
        print(f'A porra do número {num_1_float} somado com a porra do número {num_2_float} é igual a:', num_1_float + num_2_float)
    elif operador == '-':
        print(f'O caralho do número {num_1_float} subtraído com a caralha do número {num_2_float} é igual a:', num_1_float - num_2_float)
    elif operador == '*':
        print(f'O caralho do número {num_1_float} multiplicado com a caralha do número {num_2_float} é igual a:', num_1_float * num_2_float)
    elif operador == '/':
         print(f'A porra do número {num_1_float} dividido pela porra do número {num_2_float} é igual a:', num_1_float / num_2_float)
    else:
        print('Nunca deveria ter chegado aqui!!')

    print('chega né?')
    sair = input('Quer sair dessa merda inútil? [s]im: ').lower().starswith('s')

    if sair is True:
        break
    
  