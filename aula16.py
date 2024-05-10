
"""
São condicionais quando utilizamos:

if (se)
elif (se não se)
else (se não)
"""

entrada = input('Você quer "entrar" ou "sair" da caverna')

if entrada == "entrar":  #Aqui temos uma condicional de comparação boolean q funciona de forma independente
    print('Vc entrou na caverna') #Ocorre a comparação de uma variável com outra variável, podendo resultar em caminhos diferentes

elif entrada == "sair": #Esta condicional depende de um if, seria como um "segundo caminho"
    print('Vc saiu da caverna')

else:
    print('escreve certo, porra') #Esta condicional tbm depende do if, seria como um terceiro caminho
    #Como se fosse a terceira opção: se n escreveu a condicional do if, ou do elif, cairá nessa

print('Fim de código')