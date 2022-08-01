from nodo import Nodo
import webbrowser
import os

class Lista_Doble:

    def __init__(self):

        self.primero = None
        self.ultimo = None
        self.size = 0

    #insetar en lista
    def insertar(self, dato):

        nuevo = Nodo(dato)# aqui se esta creando el nodo nuevo
        self.size += 1 #aumenta el tamaño de la lista

        if self.primero == None: #aqui verifica si la lista esta vacia

            self.primero = nuevo
            self.ultimo = nuevo
        else: #si la lista no esta vacia

            self.ultimo.siguiente = nuevo #apunta hacia el nuevo nodo
            nuevo.anterior = self.ultimo #apuntamos hacia al anterior
            self.ultimo = nuevo # indica quien es el ultimos nodo ahora
    
    #mostrar datos en consola
    def imprimir(self):

        temp = self.primero # el temporal sera igual al primer nodo de la lista

        while temp != None:

            print(temp.dato) #imprime el dato que almacena el nodo

            temp = temp.siguiente #indica que el temporal ahora es igual a su nodo siguiente

    #imprime los datos al reves
    def imprimirAlreves(self):

        temp = self.ultimo
        print('Datos impresos al reves: \n')

        while temp != None:

            print(temp.dato)

            temp = temp.anterior

    def imprimir_elPrimero(self):

        print(self.primero.dato)

    #graphviz
    def graficar(self):

        graphviz = 'digraph Taller{ \n node[style=filled, fillcolor= "#FF0000", shape=box, fontcolor= white];\n edge[dir="both"] \n nodesep = 0.6; \n subgraph cluster_subContenedor { \n label="Lista Doblemente Enlazada"; \n bgcolor="#1E90FF"; \n fontcolor= white; \n  fontsize= 20; \n'

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


