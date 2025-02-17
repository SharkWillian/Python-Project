"""
1. Funções são trechos de código usados para replicar determinada ação ao longo do seu cod.
Elas podem receber valores para parâmetros (argumentos) e retornar um valor específico.
! Por padrão, funções em py retornam none (nada).

2. Argumentos nomeados tem nome com sinal de igual na frente (independe da ordem em que p argumento é passado).
3. Argumento não nomeado recebe apenas o argumento (valor) e a ordem em que é passado é dependente para execução da def.
"""

def soma(x, y): # def <nome_da_função>(<PARÂMETRO_1, PARÂMETRO_2>)
  soma = x + y
  print(f' x + y é igual a {soma}!')
 
soma(1, 2) # Ao chamar a função, deve-se passar os argumentos para que a mesma seja executada
# neste caso temos uma função com arg não nomeados (o primeiro será x e o segunfo y

soma(y=3, x=5)
# neste caso temos uma função com arg nomeados, ou seja, a ordem de x e y foram invertidas e tá TUDO bem rs
