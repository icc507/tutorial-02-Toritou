    #Problema 1  / 8 ptos x4 pruebas / 32 puntos
#Concatenación de listas o tuplas
#--------------------------------
#Confeccione un programa que lea 2 tuplas sean t1 y t2
#La salida debe ser una tupla en el orden t2 t1 t2
#---------------------------------
#Ejemplo de entrada:
#         20 90 hola
#		  mundo 44
#La salida debe ser
#         ('mundo', 44, 20, 90, 'hola', 'mundo', 44)

def tuplas(lista):
    nuevaLista = []
    for elemento in lista:
        try:
            nuevaLista.append(int(elemento))
        except ValueError:
            nuevoElemento = elemento
            nuevaLista.append(nuevoElemento)

    return tuple(nuevaLista)

t = input().split()
m = input().split()

t = tuplas(t)
m = tuplas(m)

resultado = m + t + m

print(resultado)
