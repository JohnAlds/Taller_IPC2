from cola import Cola #importamos la Cola

if __name__ == '__main__': #modulo para main

    # First In Firts Out -> Primero en Entrar Primero en Salir

    cola = Cola() #inicializamos la cola, no tiene nodos y su tamaño es de 0

    #Para este ejemplo usaremos Pokemones

    # Insertamos 5 Pokemones

    cola.encolar('Pikachu')
    cola.encolar('Bulbasaur')
    cola.encolar('Charmander')
    cola.encolar('Squirtle')
    cola.encolar('Gingar')

    cola.mostrar() # mostramos los pokemones que insertamos

    pokemon1 = cola.desencolar() # sacamos un pokemon de la cola, en este caso a Pikachu

    print( '\n' + pokemon1 + ' salio de la cola. \n') # mostramos a Pikachu

    print('Pokemones que quedaron en la cola: \n')

    cola.mostrar() #mostramos lo que ahora queda en la cola.

    #sacamos a los demas pokemones
    print('Pokemones salen de la cola: \n')
    pokemon2 = cola.desencolar()
    pokemon3 = cola.desencolar()
    pokemon4 = cola.desencolar()
    pokemon5 = cola.desencolar()

    print( '\n' + pokemon1 + ' salio de la cola. \n') # mostramos a Bulbasaur
    print( '\n' + pokemon1 + ' salio de la cola. \n') # mostramos a Charmander
    print( '\n' + pokemon1 + ' salio de la cola. \n') # mostramos a Squirtle
    print( '\n' + pokemon1 + ' salio de la cola. \n') # mostramos a Gingar

    # Si queremos sacar otro pokemon nos dire un mensaje de "Cola vacia" y retornara None

    print('----- Ya no hay nada en la cola -----')
    pokemon6 = cola.desencolar()
    print('como ya no hay nada en la cola, muestra: {}'.format(pokemon6) )



