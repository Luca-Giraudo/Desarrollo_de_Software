"""Funciones para operar sobre una lista"""
import random
lista = []

def revisar_lista(l, v):
    cantidad_mayores = 0
    for i in range(10):
        if l[i] > v:
            cantidad_mayores = cantidad_mayores + 1
    return cantidad_mayores

def calcular_promedio(l):
    suma = 0
    for i in range(10):
        suma = suma + l[i]
    promedio = suma / 10
    return promedio

def encontrar_mayor_menor(l):
    mayor = l[0]
    menor = l[0]
    for i in range(10):
        if l[i] > mayor:
            mayor = l[i]
        elif l[i] < menor:
            menor = l[i]
    return(mayor, menor)

for i in range(10):
    valor_aleatorio = random.randint(1, 20)
    lista.append(valor_aleatorio)
print("Lista de numeros aleatorios:")
print(lista)

valor = int(input("Ingresar un valor: "))
cant_mayores = revisar_lista(lista, valor)
print(f"La cantidad de valores de la lista mayores a {valor} es {cant_mayores}")

prom = calcular_promedio(lista)
print(f"El promedio de la lista es: {prom}")

(may, men) = encontrar_mayor_menor(lista)
print(f"El mayor es {may} y el menor es {men}")