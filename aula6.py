"""
CONVERSÃO DE TIPOS

Tipos imutáveis e primitivos:
str, int, float, bool
> São imutáveis pq uma vez criados, não podem ser modificados
entretanto, existem funções que podem converter alguns tipos em outros

> o operador + é um operador de polimorfismo, ou seja, possui função diferente de acordocom o tipo de valor
"""

print(1 + 1) #aqui o operador + irá SOMAR os dois valores int
print('a' + 'b') #aqui, o operador + irá CONCATENAR as duas str
print('1' + 1) #aqui o py apresentará um erro, pq os tipos de valores são diferentes (ele não pode concatenar int com str) 

print(int('1'), type(int('1'))) #Aqui a função/class int converte a str '1' em int
print(float('1') + 1) #Podemos converter um valor str em float/int e trabalhar com outros valores int/floar e vice-versa

print(bool('')) #Para variáveis booleanas, espaçoes vazios são False
print(bool('  ')) #Qualquer valor ou espaço vazio será True
print(str(11 + 'b')) #Aqui convertemos o int 11 em str e concatenamos com a str b