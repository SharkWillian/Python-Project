"""
Escopo é o local onde aquele cod pode atingir

"""

def escopo():
  x = 1 #Variável definida dentro do escopo da função / Se vc quiser utilizar esse x FORA da função, ocorrerá erros / Variável protegida pela função
  print(x) #Todo cod dentro da def, está protegido e imanipulável fora da def


x = 1
def escopo():
  global x # Add global x - declaramos q a variável x é global, logo, tudo que for modificado nessa variável terá impacto em todas variáveis x (dentro e fora)
  print(x) #Neste caso, o x utilizará do valor fora da Def, isso pode


 x = 1          # Escopo FORA do módulo/def
def escopo():   # Escopo DENTRO do módulo/def
  print(x)      # Escopo DENTRO do módulo/def
