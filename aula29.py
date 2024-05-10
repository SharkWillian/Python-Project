"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar

ERROS SÃO CHAMADOS DE EXCESSÕES 
"""
numero_str = input(
    'Vou dobrar o número que vc digitar: '
)

try: #tenta executar esse cod aqui amigão
    numero_float = float(numero_str)
    priERRO('FLOAT:', numero_float)#Aqui tem um ERRO, mas n aparece msg de erro pq o Try identica o erro e joga pro except
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except: #Se n rolar, tenta isso aqui
    print('Isso não é um número')

if numero_str.isdigit(): #Função q verifica se é td numero, se for, dá True
     numero_float = float(numero_str)
     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
else:
     print('Isso não é um número')