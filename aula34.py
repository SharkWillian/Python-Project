"""
REPETIÇÕES

WHILE (enquanto)
Executa uma ação enquanto uma condição for verdadeira

se n tiver fim, o Loop será INFINITO (enquanto for True)

"""

condicao = True

while condicao:
    nome = input('Qual seu nome? ')
    print(f'Seu nome é {nome}')
    #Neste caso, por csonta do input, 
    #o while faz o programa voltar do inicio 
    
    break #Pode-se digitar break DENTRO DO LAÇO DO WHILE, para finalizar a leitura do cod
    if nome == 'sair': #Ou fazer um if com uma palavra chave para q o cod pare
        break
print(123) #SEM O BREACK, o bloco volta do começo, então este cod fica inalcansável, mas com o breack, ele é executado  
#Ctrl C mata o programa

