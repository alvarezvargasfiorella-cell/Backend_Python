#Definir una clase
class Persona:
    pass

#constructor
class vehiculo:
        def __init__(self, color, marca, modelo): 
            self.color = color
            self.marca = marca
            self.modelo = modelo
            self.estado = "apagado"
            self.__placa = 'ABC-123'
    
        def encender(self):
            print("Encndiendo el vehículo")
            self.estado = "encendido"
            print("El vehiculo está encendido")
            self.__reiniciarvehiculo()

        def apagar(self):
            print("Apagando el vehículo")
            self.estado = "apagado"
            print("El vehiculo está apagado")

#metodo privado, no se puede acceder desde fuera de la clase, es encapulado, usa doble guion bajo al inicio
        def __reiniciarvehiculo(self):
            print("Reiniciando el vehículo")
           

#Instanciar clases, eso es crear objetos de esa clase para usar sus atributos y metodos que definimos

audi = vehiculo("rojo", "Audi", "A4")
audi.encender()
print(audi.estado)
audi.apagar()
print(audi.estado)

vw = vehiculo("azul", "Volkswagen", "Golf GTI")
print(vw._placa)

#Herencia
class animal:
     def __init__(self, nombre):
         self.nombre = nombre

class Perro(animal):
     def ladrar(self):
         print(f"{self.nombre} dice: Guau Guau!")

firulais = Perro("Firulais")
firulais.ladrar()


        