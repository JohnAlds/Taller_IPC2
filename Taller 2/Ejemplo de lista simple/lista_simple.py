
from nodo import Nodo
import webbrowser
import os

class ListaSimple:

    def __init__(self):

        self.primero = None
        self.ultimo = None
        self.size = 0

    def insertar(self, dato):

        nuevo = Nodo(dato) #creamos un nodo
        self.size += 1 #aumentamos el tamaño de la lista

        if(self.primero == None):

            self.primero = nuevo
            self.ultimo = nuevo
        else:

            self.ultimo.siguiente = nuevo #aqui insertamos
            self.ultimo = nuevo #especificamos ahora quien es el ultimo

    def mostrar(self):

        actual = self.primero

        while(actual != None):

            print(actual.dato)

            actual = actual.siguiente #recorremos la lista

    def graficar(self):

        graphviz = 'digraph Taller{ \n node[style=filled, fillcolor= "#FF0000", shape=box, fontcolor= white]; \n nodesep = 0.6; \n subgraph cluster_subContenedor { \n label="Lista Enlazada Simple"; \n bgcolor="#1E90FF"; \n fontcolor= white; \n  fontsize= 20; \n'

        #Primer paso: Creamos nodos

        actual = self.primero
        i = 1

        while(actual != None):

            graphviz += 'nodo{}[label = "{}"]; \n'.format(i, actual.dato)

            i += 1
            actual = actual.siguiente

        graphviz += '\n'

        #Segundo paso: Apuntamos cada nodo con su nodo sucesor

        actual = self.primero
        i = 1

        while(actual != None):

            if(actual.siguiente != None):

                graphviz += 'nodo{} -> nodo{}; \n'.format(i, i+1)

            actual = actual.siguiente
            i += 1

        graphviz += '\n' 

        #Tercer paso: Alinear los nodos horizontalmente

        actual = self.primero
        i = 1

        graphviz += '{rank=same'

        while(actual != None):

            graphviz += '; nodo{}'.format(i)

            i += 1
            actual = actual.siguiente

        graphviz += '}; \n }\n}'

        #print(graphviz)

        with open('grafico.txt', 'w') as file:

            file.write(graphviz)

        os.system('dot.exe -Tpdf grafico.txt -o grafico.pdf')
        webbrowser.open('grafico.pdf')







