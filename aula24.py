# Operadores IN (ESTÁ) e not in (NÃO ESTÁ)
# Strings são ITERÁVEIS (é possivel navegar entre as str)
#  0 1 2 3 4 5 (positivo)
#  O t á v i o
# -6-5-4-3-2-1 (negativo)

nome = 'Otávio'
print(nome[2]) #busca Positivo (esq pra dir)
print(nome[-4]) #busca negativo (dir pra esq)

print('vio' in nome) #As str vio ESTÃO na variavel nome?
print('zero' in nome) #As str zero ESTÃO na variavel nome?
print(10 * '-')
print('vio' not in nome) #As str vio NÃO ESTÃO na variavel nome?
print('zero' not in nome) #As str zero NÃO ESTÃO na variavel nome?

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')