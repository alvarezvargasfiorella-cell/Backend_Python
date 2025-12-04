""" Crear una aplicacion que simule un cajero 
automatico, del cual puedas retirar y pedositar dinero,
ademas de consultar el saldo disponible. """

import os
class cajero:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Saldo insuficiente.")
            return
        else:
            self.saldo -= cantidad
            print(f"Has retirado {cantidad}. Saldo restante: {self.saldo}")

    def depositar(self, cantidad):
        if cantidad <= 0:
            print("Cantidad invalida.")
            return
        self.saldo += cantidad
        print(f"Has depositado {cantidad}. Saldo actual: {self.saldo}") 

    def ver_saldo(self):
        print(f"Saldo disponible: {self.saldo}")

cajero = cajero () 

while True:
    2
    os.system("clear")
    print("""
    ==========================
        Cajero Automático
    ==========================
    1. Retirar Dinero
    2. Depositar Dinero
    3. Consultar Saldo
    4. Salir
    ==========================
    """)
    opcion = input("Elija una opción: ")
    if opcion == "1":
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        cajero.retirar(cantidad)
    elif opcion == "2":
        cantidad = float(input("Ingrese la cantidad a depositar: "))
        cajero.depositar(cantidad)
    elif opcion == "3":
        cajero.ver_saldo()
    elif opcion == "4":
        print("Gracias por usar el cajero automático. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, intente de nuevo.")
        input("Presione Enter para continuar...")