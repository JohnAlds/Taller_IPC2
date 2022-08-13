#importaciones de modulos
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

    listaE = rutas.cargarEntrenadores()

    print()
    listaE.mostrarEntrenadores()

        
    
        
        