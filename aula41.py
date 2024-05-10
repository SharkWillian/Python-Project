""" while/else """
string = 'Valor qualquer'

i = 0 # i é comumente utilizado para descrever índices
while i < len(string): #quando i for menor q o total de letras da string
    letra = string[i] 

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
print('Fora do while.')