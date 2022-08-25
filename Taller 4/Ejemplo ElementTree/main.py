#importaciones de modulos
from clases import Entrenador
from lista_doble import Lista_Doble

if __name__ == '__main__':

    n = 0
    rutas = Lista_Doble()

    while( n != 2):

        print('Ingrese la ruta de su archivo: \n')

        ruta = input('\t →  ')

        rutas.insertar(ruta)

        print('¿Quiere agregar otro archivo? \n')
        print('→ 1. Si')
        print('→ 2. No\n')

        n = int(input('Digite la opción a realizar: '))

    listaE = rutas.cargarEntrenadores() #aqui tenemos nuestra lista de entrenadores ya cargada con los datos del xml

    print()
    #listaE.mostrarEntrenadores() # imprimimos en consola los entrenadores que tenemos

    n1 = 0

    while n1 != 2:

        nombre = input('Ingrese el nombre del entrenador que desea buscar: ')
        print()

        entrenador : Entrenador = listaE.obtenerEntrenador(nombre) #pasamos el nombre del entrenador que deseamos buscar

        print('''Entrenador: {}
        edad: {}
        medallas: {}'''.format(entrenador.nombre, entrenador.edad, entrenador.medallas))

        print('¿Quiere buscar otro entrenador? \n')
        print('→ 1. Si')
        print('→ 2. No\n')

        n1 = int(input('Digite la opción a realizar: '))
        print()


    #aqui obtenemos el elemento que esta en la posicion 2 de la lista
    entrenador1 = listaE.obtenerElemento(2)

    print('''Entrenador: {}
        edad: {}
        medallas: {}'''.format(entrenador1.nombre, entrenador1.edad, entrenador1.medallas))






        
    
        
        