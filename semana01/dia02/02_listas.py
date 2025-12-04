lista1 = [1,2,3,4,5]
lista2 = ["manzana", "pera", "uva"]
lista3 = [1, "hola", True, 3.14]
lista4 = []
lista5 = [[1,2], [3,4], [5,6]]


# Acceder a sus elementos
print(lista1[0])  # Primer elemento de lista1
print(lista2[1])  # Segundo elemento de lista2
print(lista3[2])  # Tercer elemento de lista3

print(lista2[-1])  # Último elemento de lista2

print(lista2[len(lista2) - 1])  # Último elemento de lista2 usando len()})
print(lista5[1][0])  # Primer elemento del segundo sublista en lista5

#slicing
print(lista1[1:4])  # Elementos desde el índice 1 hasta el 
print(lista1[1:4:2]) # Elementos desde el índice 1 hasta el 4 con paso 2
print(lista2[:2])   # Primeros dos elementos de lista2
print(lista2[2:])   # Desde el tercer elemento hasta el final de lista3

#modificar elementos
lista1[0] = 10
print(lista1)

#obtener la longitud de una lista
print("longitud de lista2:", len(lista1))

#metodos de listas
lista4.append(6)
