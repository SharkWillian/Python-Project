"""
Listas em Py
Tipo list - mutável
Suporta vários valores de qualquer tipo
Métodos úteis: append; insert; pop; del; clear; extend+
"""
lista = [123, True, 'Will Reina', 1.2, []]
print(lista, type(lista)) #o type será list
#Podemos colocar qualquer tipo de item

print(lista[2]) #aqui podemos exibir o item 2 da list

lista[2] = 'Willian Reina' #aqui podemos modificar um item da lista
print(lista[2]) #aqui temos o item modificado

#nome = lista[2] #Pode-se armazenar um item da lista em uma variável
#print(nome)

#del lista[2] #Aqui podemos deletar um item da lista
#print(lista[2]) #E seguindo o infice teremos um novo item 2

#se vc possuí uma lista mt extensa, é interessante evitar usar o del, pois o programa terá que reorganizar todo índice da lista e pode quebrar códigos q a acessem etc
lista.append('Joviano')
lista.append(20)
print(lista)

#Com append, podemos adicionar itens ao final da lista
lista.pop() #remove o último item da lista
