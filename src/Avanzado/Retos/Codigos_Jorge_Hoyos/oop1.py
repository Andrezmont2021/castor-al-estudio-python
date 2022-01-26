# Programación orientada a objetos, primera parte. + Encapsulación de propiedades 
class Coche:
    # Propiedades, estado inicial encapsulado
    def __init__(self):
        self.__largo_chasis = 250
        self.__ancho = 120
        self.__ruedas = 4
        self.__marcha = False

    # Comportamientos (¿Qué puede hacer? arrancar, frenar, girar...)
    def arrancar(self, arranca):
        self.__marcha = arranca

        if self.__marcha:
            chequeo = self.__chequeo_interno()
        if self.__marcha and chequeo:
            return "El carro está en marcha"
        elif self.__marcha and chequeo == False:
            return "Algo ha salido mal en el chequeo, no se puede arrancar"
        else :
            return "El carro está parado"

    def estado(self):
        print(f"El carro tiene {self.__ruedas} ruedas. Un ancho de {self.__ancho} y un largo de {self.__largo_chasis}")

    # Método encapsulado, solo accesible a través del método arrancar
    def __chequeo_interno(self):   
        print("Realizando chequeo interno")
        
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas":
            return True
        else:
            return False

mi_donkey = Coche()
print(mi_donkey.arrancar(True))
mi_donkey.estado()

print("----------A continuación creamos la segunda instancia (segundo objeto)------------")

tu_donkey = Coche()
print(tu_donkey.arrancar(False))
tu_donkey.__ruedas = 2
tu_donkey.estado()