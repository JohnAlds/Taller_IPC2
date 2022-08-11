from nodo import Nodo

class Cola:

    def __init__(self): # constructor
        
        self.primero = None # Tendremos un nodo primero que esta siempre al frente de la cola.
        self.ultimo = None # Al final de la cola tendremos siempre un nodo ultimo.
        self.size = 0 # La cola tendra un tamaño pero inicialmente es 0. 

    # insertar(encolar)
    def encolar(self, dato): # insertar al final de la cola.

        nuevo = Nodo(dato) # creamos un nodo que contendra el dato que le pasemos al metodo.
        self.size += 1 # aumentamos en 1 el tamaño porque vamos a insertar un dato.

        if(self.primero == None): # Si el primer nodo de la cola es None quiere decir que esta vacia.

            self.primero = self.ultimo = nuevo # como es el primer nodo que insertamos en la cola, el primero y el ultimo seran el nuevo nodo.
        else: # En caso el primero de la lista no sea None significa que ya hay elementos en la cola e insertaremos uno nuevo.

            self.ultimo.siguiente = nuevo # aqui indicamos que el ultimo apunta al nuevo nodo que creamos.
            self.ultimo = nuevo # ahora el nuevo nodo sera el ultimo de la cola.
    
    # Desencolar
    def desencolar(self): # eliminaremos el primer nodo de la cola y retornamos el dato que contenia.

        if self.primero is None: # si el primero es None, la cola esta vacia

            print('Cola vacía.')
            return None # retornamos None para indicar que la cola esta vacia
        else: # Si no esta vacia haremos lo siguiente

            temp = self.primero.dato # almacenamos el dato del primer nodo en una variable temporal

            if self.primero is self.ultimo: # Si el primero nodo es igual al ultimo nodo quiere decir que solo hay 1 nodo en la cola.

                self.primero = self.ultimo = None # restablecemos el primero y ultimo de la cola.
                self.size -= 1 # disminuimos en 1, porque eliminamos 1 nodo.

                return temp # retornamos el dato que almacenamos en temp
            else: #Si no, quiere decir que hay ma de un elemento en la cola

                self.primero = self.primero.siguiente # ahora el primer nodo sera el siguiente del que ERA el primero
                self.size -= 1 # disminuimos en 1 porque eliminamos un nodo de la cola

                return temp # retornamos el dato que almacenamos en temp

    # Mostrar
    def mostrar(self):

        actual = self.primero # comenzara en el primer nodo de la cola

        while(actual != None): 

            print(actual.dato) #imprimimos el dato que contiene el nodo en consola

            actual = actual.siguiente # pasamos al nodo que le sigue al actual






    