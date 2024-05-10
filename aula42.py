frase = 'O py é uma linguadem de programação '\
    'multiparadigma. '\
    'py doi criado por Guido van Rossum'.upper()#.lower = letras minúsculas ou upper = letras maiúsculas

#Para quebrar a linha, pode-se usar \, preservando as aspas str

#print(frase.count('py'))

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    quantas_vezes_letra_apareceu_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < quantas_vezes_letra_apareceu_atual:
        qtd_apareceu_mais_vezes = quantas_vezes_letra_apareceu_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(f'A letra que apareceu mais vezes foi {letra_apareceu_mais_vezes} que apareceu {qtd_apareceu_mais_vezes}')