
class FiguraGeometrica:

    def __init__(self, numLados, longintud):

        self.__numLados = numLados
        self.__longitudL = longintud


    def perimetro(self):

        perimetro = self.__numLados*self.__longitudL

        print(  'El perimetro de la figura es: ' + str(perimetro))

    #Getters
    def getNumLados(self):

        return self.__numLados

    def getLongitudL(self):

        return self.__longitudL
    
    #Setters
    def setNumLados(self, numLados):

        self.__numLados = numLados

    def setLongitudL(self, longintudL):

        self.__longitudL = longintudL



    

class Cuadrado(FiguraGeometrica):

    def __init__(self, numLados, longintud, sumaAngulos):

        self.sumaAngulos = sumaAngulos
        super().__init__(numLados, longintud) #hereda atributos de la clase padre

    def perimetro(self):

        perimetroC = 4* self.longitudL

        print('El perimetro del Cuadrado es: {}'.format(perimetroC))

        


class Triangulo(FiguraGeometrica):

    def __init__(self, numLados, longintud):
        self.sumaAngulos = '180 grados'
        super().__init__(numLados, longintud)
    
    def perimetro(self):

        perimetroT = 3* self.longitudL

        print('El perimetro del Triangulo es:' + str(perimetroT))

class Persona:

    def __init__(self, nombre, dpi, mascota):
        
        self.nombre = nombre
        self.dpi = dpi
        self.mascota = mascota

class Perro:

    def __init__(self, nombre, raza):

        self.nombre = nombre
        self.raza = raza
    


           


