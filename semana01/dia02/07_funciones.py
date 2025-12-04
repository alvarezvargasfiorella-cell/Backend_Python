def sumar(a,b):
    return a + b

# resultado=sumar(5, 10)
# print(resultado)

# funcion con valor por defecto
def saludar(nombre="Invitado"):
    print(f"Hola, {nombre}!")

saludar()

#funciones con n argumentos (*args), *args es una tupla internamente que almacena los argumentos
def mostrar_numeros(*numeros):
    for numero in numeros:
        print(numeros)

mostrar_numeros(1,"Hola", True)

#funciones con n argumentos nombrados (**kwargs), **kwars es un diccionario internamente que almacena los argumentos nombrados
def mostrar_info(**info):
    for clave, valor in info.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Ana", edad=30)