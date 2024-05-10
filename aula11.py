"""
Precedência de operadores:
1. (n + n)
2. **
3. * / // %
4. + -

Essa é a ordem em que os operadores
serão executados numa equação em Py.
"""

conta_1 = (1 + 1) ** (5 + 5)
print(conta_1)

conta_2 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_2)