from nodo import Nodo
from clases import Entrenador, Pokemon

#ElementTree
import xml.etree.ElementTree as ET

class Lista_Doble:

    def __init__(self):

        self.primero = None
        self.ultimo = None
        self.size = 0

    #insetar en lista
    def insertar(self, dato):

        nuevo = Nodo(dato)
        self.size += 1 

        if self.primero == None: 

            self.primero = nuevo
            self.ultimo = nuevo
        else: 

            self.ultimo.siguiente = nuevo 
            nuevo.anterior = self.ultimo 
            self.ultimo = nuevo 
    
    #mostrar datos en consola
    def mostrar(self):

        temp = self.primero 

        while temp != None:

            print(temp.dato) 

            temp = temp.siguiente 
    
    def cargarEntrenadores(self):

        actual = self.primero

        #Lista para los entrenadores
        listaEntrenadores = Lista_Doble()

        #atributos de un entrenador
        nombreE = ''
        edad = 0
        medallas = 0
        pokeballs = 0
        pokemones = Lista_Doble()

        #atributos de pokemon
        nombreP = ''
        tipo = ''


        while actual != None:

            tree = ET.parse(actual.dato) 
            root = tree.getroot() #obtengo la etiqueta raíz

            for elemento in root: # elemento es la etiqueta <entrenador>

                if elemento.tag == 'entrenador':

                    for subelemento in elemento: # subelemento sera la etiquetas que tienen un nivel menos, en este caso <datosentrenador> <medallas> <pokeballs> <pokemones>

                        if subelemento.tag == 'datosentrenador': # si es la etiqueta <datosentrenador>

                            for sub in subelemento: # sub sera las etiquetas <nombre> <edad>

                                if sub.tag == 'nombre': # si es la etiqueta <nombre>

                                    nombreE = sub.text
                                    #print(nombreE)
                                elif sub.tag == 'edad': # si es la etiqueta <edad>

                                    edad = int(sub.text) # la propiedad "text" me devuelve un cadena con int() lo convierto a entero
                                    #print(edad)

                        elif subelemento.tag == 'medallas': # si es la etiqueta <medallas>

                            medallas = int(subelemento.text) # la propiedad "text" me devuelve un cadena con int() lo convierto a entero
                            #print(medallas)
                        
                        elif subelemento.tag == 'pokeballs': # si es la etiqueta <pokeballs>

                            pokeballs = int(subelemento.text) # la propiedad "text" me devuelve un cadena con int() lo convierto a entero
                            #print(pokeballs)

                        elif subelemento.tag == 'pokemones': # si es la etiqueta <pokemones>

                            for sub in subelemento: # sub sera la etiqueta <pokemon>

                                if sub.tag == 'pokemon': # si es la etiqueta <pokemon>

                                    nombreP = sub.get('nombre') # obtengo el nombre del pokemon
                                    tipo = sub.get('tipo') # obtengo el tipo del pokemon

                                    #print(nombreP + ' ' +tipo)

                                    pokemon = Pokemon(nombreP, tipo) # creo un objeto pokemon
                                    pokemones.insertar(pokemon) # inserto un pokemon en la lista pokemones 

                #print('-----------------------------------------')
                entrenador = Entrenador(nombreE, edad, medallas, pokeballs, pokemones) # creo un objeto Entrenador
                listaEntrenadores.insertar(entrenador) # inserto un entrenador en la lista entrenadores

                #limpiar la lista pokemones
                pokemones = Lista_Doble()

            actual = actual.siguiente #pasamos a la siguiente ruta un archivo xml, siempre que hayamos agregado mas.

        return listaEntrenadores # retornamos la lista de entrenadores

    def mostrarEntrenadores(self):

        temp = self.primero 

        while temp != None:

            print('------------------------------------\nEntrenador: {}\nEdad: {}\nMedallas: {}\nPokeballs: {}\n\nPokemones:\n\n'.format(temp.dato.nombre, temp.dato.edad, temp.dato.medallas, temp.dato.pokeball)) 

            temp.dato.pokemones.mostrarPokemones()

            temp = temp.siguiente 
    
    def mostrarPokemones(self):
        
        temp = self.primero 

        while temp != None:

            print('Nombre: {}\nTipo: {}\n'.format(temp.dato.nombre, temp.dato.tipo)) 

            temp = temp.siguiente

    #obtener entrenador deseado por el nombre
    def obtenerEntrenador(self, nombreE):

        temp = self.primero

        while temp != None:

            if nombreE.lower() == temp.dato.nombre.lower(): #cuando encuentre el elemento deseado retornara el dato que contiene el nodo, en este caso un entrenador el cual fue buscado por su nombre

                return temp.dato # se retorna el dato
            
            temp = temp.siguiente #el temp recorre la lista
        
        if temp == None: #en el caso que no se haya encontrado el entrenador, mostrara el siguiente mensaje en consola.

            print('Entrenador no encontrado.') #mensaje en caso no encuentre el entrenador

    #obtener un elemento por la posición en la lista
    def obtenerElemento(self, posicion):

        i = 1 #nuestra lista comienza en la posición 1
        temp = self.primero

        while temp != None:

            if i == posicion:

                return temp.dato

            i += 1
            temp = temp.siguiente
        
        if temp == None:

            print('Elemento no encontrado.')

