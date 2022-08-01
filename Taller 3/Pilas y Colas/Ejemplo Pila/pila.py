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

        if self.size == 0:

            print('La pila esta vacia, no se puede obtener la cima.')
        else:

            cimaR = self.cima
            temp = self.primero

            if temp.arriba != None:

                while temp.arriba != self.cima:

                    temp = temp.arriba
            
            
                temp.arriba = None
                self.cima = temp
                self.size -= 1

                return cimaR.dato
            else:

                cimaR = self.cima
                self.cima = self.primero = None
                self.size -= 1

                return cimaR.dato

    def mostrar(self):

        temp = self.primero

        while(temp != None):

            print(temp.dato)

            temp = temp.arriba #recorremos la pila

    