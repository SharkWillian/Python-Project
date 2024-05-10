lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
print(lista_c)
#O operador + pode concatenar o type list

lista_a.extend(lista_b)
print(lista_a)


#A função EXTEND mexe diretamente na lista do primeiro argumento, extendendo com  segunda lista relacionada
