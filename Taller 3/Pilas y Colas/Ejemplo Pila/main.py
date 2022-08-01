from doctest import OutputChecker
from pila import Pila

#Last In Firts Out - Pila

pila = Pila()

pila.push(1)
pila.push(2)
pila.push(3)
pila.push(4) # --- ultimo elemento en entrar

print('Sacamos un dato de la pila: \n')
numero = pila.pop()
print(numero)

print('Después de haber sacado de la pila: \n')
pila.mostrar()

print('Sacamos un dato de la pila: \n')
numero = pila.pop()
print(numero)

print('Después de haber sacado de la pila: \n')
pila.mostrar()

print(pila.pop())
print(pila.pop())

pila.pop()

