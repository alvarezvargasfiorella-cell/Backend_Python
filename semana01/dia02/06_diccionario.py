usuario ={
    "id": 1,
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid",
}

#Acceder a los elementos del diccionario
print(usuario["nombre"])  # Acceder al valor asociado a la clave "nombre"
print(usuario.get("nombre", "no disponible"))  # Acceder al valor asociado a la clave "edad" usando get()
print(usuario.get("pais", "no disponible"))  # Intentar acceder a una clave inexistente con valor por defecto

usuario["edad"] = 26  # Modificar el valor asociado a la clave "edad"
usuario["genero"] = "Femenino"  # Agregar una nueva clave-valor al diccionario
print(usuario)

#Eliminar elementos del diccionario
del usuario["ciudad"]  # Eliminar la clave "ciudad" usando del
usuario.pop("genero")  # Eliminar la clave "genero" usando pop()

#metodos de diccionarios
print(usuario.keys())    # Obtener todas las claves del diccionario
print(usuario.values())  # Obtener todos los valores del diccionario
print(usuario.items())   # Obtener todos los pares clave-valor del diccionario