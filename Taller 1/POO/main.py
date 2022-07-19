from clases import FiguraGeometrica, Cuadrado, Triangulo, Perro, Persona


# Main 

figura = FiguraGeometrica(5, 3)
#figura2 = FiguraGeometrica(7, 4)

#c1 = Cuadrado(4, 4, 360)
#t1 = Triangulo(3, 10)
#figura.perimetro()
#c1.perimetro()
#t1.perimetro()

#print( figura.getNumLados()) # ---- 5
figura.setNumLados(10) # ---- modifique el atributo de este objeto
#print( figura.getNumLados()) # ----- 10

#---------------------------------------------------------------------------------

perro = Perro('Bruno', 'Beagle')
persona = Persona('Jose', '213215854554', perro)

print( 'Nombre de la persona: {} Nombre de la mascota: {}'.format(persona.nombre, persona.mascota.nombre ))

