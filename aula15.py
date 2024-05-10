#A função input é utilizada para coletar dados do usuário
#A interação ocorre apenas no terminal

#input('Qual é o seu nome? ')

nome = input('Qual seu nome? ')
print(f'O seu nome é {nome}')

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

print(f'A soma dos dois números é: {numero_1 + numero_2}')
"""
Aqui encontramos um erro, 1 + 5 n é 15, o q aconteceu é q a função 
input coleta dados como str, e o operador + concatena os dois valores
inputados.

Para q isso dê certo, é necessario fazer a converção de str para int/float
"""

numero_3 = int(input('Digite um número (agr vai): '))
numero_4 = int(input('Digite outro número (agr vai MESMO): '))

print(f'A soma dos dois números é: {numero_3 + numero_4}')

