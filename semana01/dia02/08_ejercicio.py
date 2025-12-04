#Crear una aplicacion para gestionar usuarios. donde podemos agregar, mostrar, actualizar y eliminar usuarios (CRUD)

usuarios = {
    "787878787": {
        "nombre": "Ana",
        "correo": "ana@gmail.com"
    }
}

while True:
    print("""
    ==========================
    Gestor de Usuarios
    ==========================
    1. Agregar Usuario
    2. Mostrar Usuarios
    3. Actualizar Usuario
    4. Eliminar Usuario
    5. Salir
    ==========================""")
    opcion = imput("Elija una opción:")
    print(opcion)

    if opcion == "1":
        dni = input("DNI")
        nombre = input("Nombre:")
        correo = input("Correo:")

        usuarios[dni] = {
            'nombre': nombre,
            'correo': correo
        }

        print("Usuario agregado exitosamente.")
        input("Presione enter para volver al menu")
        
    if opcion == "2":
        for dni, usuario in usuarios.items():
            print(f"DNI: {dni}")
            print(f"Nombre: {usuario['nombre']}")
            print(f"Correo: {usuario['correo']}\n")
            print("-----------------------")
    if opcion == "3":
        pass
    if opcion == "4":
        pass
    if opcion == "5":
        pass
    else:
        print("Opcion incorrecta, intente de nuevo.")
        input("Presione enter para volver al menu")