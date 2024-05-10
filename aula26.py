"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f    {valor float:.2F} (DEFINE O Nº DE CASAS DECIMAIS Q VC QUER)
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') #DIZ Q A VARIÁVEL DEVERÁ TER 10 CARACTERES A DIREITA
print(f'{variavel: <10}.') #DIZ Q A VARIÁVEL DEVERÁ TER 10 CARACTERES A ESQUERDA
print(f'{variavel: ^10}.') #ADICIONA 10 CARACTERES NO CENTRO
print(f'{1000.4873648123746:.1f}') #Definindo casas decimais
print(f'{1000.4873648123746:,.1f}') #Se add uma virgula depois dos :, vc define a separação de bilhar ex: 1,000.4
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')