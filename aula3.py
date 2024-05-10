"""
python = Linguagem de programação
tipagem = dinâmica / forte (O py reconhece os tipos de variáveis automaticamente)
*Linguagens de tipagem estática, deve-se informar os tipos de dados manualmente.

str > string > texto
Strings são textos, SEMPRE representados entre aspas

Lembrando de sempre quando for utilizar aspas simples, iniciar e fechar com aspas simples. A mesma coisa com aspas duplas
"""

print('123') # Os números por estarem entre aspas serão interpretados como textos
print("Hello, mundão") # O py exibe o texto entre aspas, interpretando como string

#Escape (\antes de aspas)
print("Luiz \"Otávio\"") #Ao utilizar a \ o interpretador de py automaticamente ignora o próximo caracter.

#Para utilizar aspas dentro de um argumento sem que o código dê ruim
#ou que se use a \, é só incluir aspas simples dentro de duplas ou vice-versa

print('Luiz "Otávio"')
print("Luis 'Otávio'")
