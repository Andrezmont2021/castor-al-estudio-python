class Coche:
    # Propiedades
    largo_chasis = 250
    ancho = 120
    ruedas = 4
    marcha = False

    # Comportamientos (¿Qué puede hacer? arrancar, frenar, girar...)
    def arrancar(self):
        self.marcha = True

    def estado (self):
        if self.marcha == True:
            return "El carro está en marcha"
        else :
            return "El coche está parado"

mi_donkey =Coche()
print(f"El largo del carro es {mi_donkey.largo_chasis}")
print(f"El carro tiene {mi_donkey.ruedas} ruedas")
mi_donkey.arrancar()

print(mi_donkey.estado())