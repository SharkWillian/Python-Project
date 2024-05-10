nome = 'Daniel Reina Ferreira'
altura = 1.75
peso = 70.0

imc = int(peso / altura ** 2) 

print(nome, 'tem' , altura, 'de altura,', 'pesa', peso, 'Kg,', 'e seu IMC é', imc, 'Kg/M2') 
#Outra forma de executar esse print, é utilizando "F STRINGS" (Format Strings) que irão utlizar fórmulas dentro das strings

print(f'{nome} tem {altura} metros de altura, pesa {peso}Kg, e seu IMC é {imc}Kg/M2')
# Aqui coloca-se a letra f antes da string, e as operações entre chaves {}, neste caso, cahmando as variáveis.