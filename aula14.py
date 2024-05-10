 
a = 'A'
b = 'B'
c = 1.1
string = 'a={} b={} c={}' # Aqui as chaves referenciam a ordem 0, 1 e 2 dos argumentos passados no método format
formato = string.format(a, b, c)
print(formato)

"""
Tudo dentro do Py é um objeto
quando utilizamos . temos uma FUNÇÃO, e quando essa função está dentro de um objeto ela torna-se um MÉTODO

"""

a = 'A'
b = 'B'
c = 1.1
string1 = 'a={chaveA} b={chaveB} c={chaveC} d={chaveA}' 
formato1 = string1.format(chaveA = a, chaveB = b, chaveC = c)
# Aqui as chaves referenciam a os PARÂMETROS NOMEADOS, então é possível chamar os argumentos fora da ordem, exatamente por estarem todos noemados
print(formato1)