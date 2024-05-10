# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor
# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123'

#Aqui o AND permite que duas condições sejam avaliadas
# na mesma sentênça do IF

#Se a primeira condição (entrada == E) for True, ele passa
#para a segunda condição (SenhaD == SenhaP), e se for True
#Ele segue a execução do código. 
#Se alguma sentença for False (tanto if quanto and), ele segue para Else (Sair)
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliação de curto circuito
# QUANDO USADO O AND e tiver algo (qualquer coisa) falso = dá falso
# Quando tiver somente condições bool True, daí sim dá true
print(True and False and True) 
print(True and 0 and True) #Aqui, ele retorna o valor 0

if 0 and 1: # Aqui o 0 do if é um FALSY, logo a sentença é falsa e nada é exibido
    print(True and 1) 