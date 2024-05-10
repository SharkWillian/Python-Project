"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

entrada = input('Digite um numero: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')

else:
    print('Vc n digitou um número inteiro')

# ou

entrada = input('Digite um numero inteiro: ')

try:
    entrada.isdigit()
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')

except:
    print('Vc n digitou um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
entrada2 = int(input('Q horas são? (Em números int) '))

madruga = entrada2 >= 00 and entrada2 <= 4
bom_dia = entrada2 >= 5 and entrada2 <= 12
boa_tarde = entrada2 >= 13 and entrada2 <= 18
boa_noite = entrada2 >= 19 and entrada2 <= 23

try:
    if madruga:
        print('oloco, vai dormir maluco!')
    if bom_dia:
        print('Buenos dias')
    if boa_tarde:
        print('Buenas tardes')
    if boa_noite:
        print('Buenas notches')

except:
    print('Vc n digitou um número válido')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

entrada3 = len(input('Escreva seu primeiro nome: '))

nominho = entrada3 <= 4 
nome = entrada3 > 5 and entrada3 <= 6
nomezaum = entrada3 > 6

try:
    if nominho:
        print('Seu nome é curto')
    if nome:
        print('Seu nome é normal')
    if nomezaum:
        print('Seu nome é muito grande')
#    else:
#        print('Seu nome é mt grande') # PODE FECHAR COM ELSE, JÁ Q TD Q FOR MAIOR É ISSO
except:
    print('Escreve direito pq n sou obrigada!')

print('Arrasou korolhon')