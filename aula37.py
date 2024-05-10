contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('não vou mostrar o 6')
        continue #Ele PULA o trecho correspondente ao true

    if contador >= 10 and contador <= 27:
        print('N vou mostrar o', contador)
        continue
        
    print(contador)

    if contador == 40:
        break

print('game over')
