from doctest import OutputChecker
from pila import Pila

#Last In Firts Out - Pila

pila = Pila()

pila.push(1) # --- primero en entrar
pila.push(2)
pila.push(3)
pila.push(4) # --- ultimo elemento en entrar

print('Sacamos un dato de la pila: \n')
numero = pila.pop() # saca de la pila el numero 4
print(numero) #lo imprime

print('Después de haber sacado de la pila: \n')
pila.mostrar() #muestra los numeros que quedan, en este caso el 3, 2 y 1

print('Sacamos un dato de la pila: \n')
numero = pila.pop() # saca de la pila el numero 3
print(numero) # lo imprime

print('Después de haber sacado de la pila: \n')
pila.mostrar() #imprime los numeros que quedan, en este caso 2 y 1

print(pila.pop()) # imprime 2
print(pila.pop()) # imprime 3

pila.pop()

