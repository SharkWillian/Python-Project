"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear() Limpa a lista

lista.insert(100, 5)
#Aqui. usando a função insert, pode-se escolher o valor e em qual ÍNDICE add o valor
#lista.insert(arg1(valor ára add), arg2(posição no indice para add) )
print(lista[4])

#Append add no final / inert vc pode escolher a posição
