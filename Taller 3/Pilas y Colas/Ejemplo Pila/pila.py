from nodo import Nodo

class Pila:

    def __init__(self):

        self.cima = None
        self.primero = None
        self.size = 0

    def push(self, dato):

        nuevo = Nodo(dato)
        self.size += 1

        if(self.primero == None):

            self.cima = self.primero = nuevo 
        else:

            self.cima.arriba = nuevo
            self.cima = nuevo

    def pop(self):

        if self.size == 0: # si la pila esta vacia, hace lo siguiente

            print('La pila esta vacia, no se puede obtener la cima.')
        else: # si ya hay elementos en la pila hace lo siguiente

            cimaR = self.cima # guardamos la cima en una variable 
            temp = self.primero # temporal es el primer nodo de la pila

            if temp.arriba != None: # si el apuntador del primer nodo de la pila es diferente de None, quiere decir que hay mas de 1 elemento en la pila

                while temp.arriba != self.cima: # recorre la pila desde el primer nodo hasta el penultimo nodo.

                    temp = temp.arriba # el temporal ahora sera el nodo que que se encuentre arriba(recorre)
            
            
                temp.arriba = None # Eliminamos la cima
                self.cima = temp # ahora la cima sera el penultimo nodo
                self.size -= 1 # disminuimos en 1 el tamaño de la pila, porque eliminamos 1 elemento

                return cimaR.dato # retornamos el dato que contenia el nodo que  "ERA LA CIMA" <--- atención a esto

            else: # Si el apuntador hacia arriba del temporal es None, quiere decir que hay un elemento en la pila 
 
                self.cima = self.primero = None # El primero y la cima de la pila ahora es None, porque ya no hay mas elementos en la pila
                self.size -= 1 # disminuimos el tamaño de la pila, porque eliminamos 1 elemento de la pila, en este caso el ultimo que quedaba

                return cimaR.dato # retornamos el dato que contenia la cima, cuando aun existia. 

    def mostrar(self):

        temp = self.primero

        while(temp != None):

            print(temp.dato)

            temp = temp.arriba #recorremos la pila

    