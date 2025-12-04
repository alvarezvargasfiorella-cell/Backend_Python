frutas = ["manzana", "pera", "platano", "uva","papaya"]
#iterar cadenas de caracteres
cadena = "Hola, mundo!"
for caracter in cadena:
    print(caracter)
#iterar diccionarios
diccionario = {
    "nombre": "Ana", 
    "edad": 25, 
    "ciudad": "Madrid"}
for clave in diccionario:
    print(clave) #imprime las claves)

for index, valor in enumerate(frutas):
    print(index, valor)

#bucles anidados

letras = ["A", "B", "C", "D"]
numeros = [1, 2, 3, 4]
for letra in letras:
    for numero in numeros:
        print(letra, numero)

#control de flujo (break y continue)
animales = ["perro", "gato", "loro","pez", "raton"]

for animal in animales:
    if animal == "loro":
        print("Loro encontrado, saliendo del bucle.")
        break
    print(animal)

for animal in animales:
    if animal == "loro":
        print("Loro encontrado, saltando este animal.")
        continue
    print(animal)

#list comprehensions
nuevos_animales=[]
for animal in animales:
    nuevos_animales.append(animal.upper()) #convertir a mayusculas

print(nuevos_animales)