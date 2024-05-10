"""
Fatiamento de strings
 012345678 9positivo começa do 0
 Olá mundo
-987654321 negativo começa do -1
Fatiamento [i:f:p] [::] [INICIO:FINAL:PASSO]Aqui a str é literalmente fatiada
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[4:]) #Se vc omite o final, então ele pega o indice q vc colocou e vai até o fim
print(variavel[3:9]) #Se vc define o final, ele pega até onde vc definiu
print(variavel[-5:-4])
print(len(variavel[-5:-4])) #Função LEN quantifica a quantidade de CARACTERES
print(len(variavel))

#Considerando [i:f:p] onde o p, representa de quantos em quantos caracteres será feita a leitura/fatiamento

print(variavel[0:9:2]) #O 2 é a de quantos em quantos caracteres serão pulados
print(variavel[-1:-9:-2]) #Essa contagem pode ser negativa tbm (da dir pra esq)
