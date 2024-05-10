nome = input('Qual o meu nome? ')
idade = input('Quantos anos VC tem? ')

if nome and idade: #LEMBRANDO q se n tiver valores nessas variaveis, o if considera FALSE, e nada é executado, vai td pro else
    print(f'Seu nome é {nome}!')
    print(f'Seu nome invertido é {nome[::-1]}')
    
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    
    letras = len(nome)
    print(f'Seu nome contém {letras} letras)')
    print(f'Seu nome tem {len(nome)} letras') #Pode ser assim tbm
    print(f'A primeira letra do seu nome é {nome[0]}') #Primeiro da Esq pra Dir
    print(f'A última letra do seu nome é {nome[-1]}') #Primeiro da Dir pra Esq
else:
    print('Você deixou campos vazios')