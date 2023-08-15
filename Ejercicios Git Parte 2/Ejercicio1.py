opcion = 0
senial = 0
while opcion != 7:
    print("MENU\n1. Ingresar valor 1\n2. Ingresar valor 2\n3. Mostrar suma\n4. Mostrar resta\n5. Mostrar multiplicación\n6. Mostrar división\n7. Salir")
    opcion = int(input("\nIngresar opcion: "))

    if opcion == 1:
        valor1 = int(input("Ingresar el valor 1: "))
        senial = senial + 1
    elif opcion == 2:
        valor2 = int(input("Ingresar el valor 2: "))
        senial = senial + 1
    elif opcion == 3:
        if senial < 2:
            print("ERROR. Ingresar primero los dos valores")
        else:
            print(f"SUMA: {valor1 + valor2}")
    elif opcion == 4:
        if senial < 2:
            print("ERROR. Ingresar primero los dos valores")
        else:
            print(f"RESTA: {valor1 - valor2}")
    elif opcion == 5:
        if senial < 2:
            print("ERROR. Ingresar primero los dos valores")
        else:
            print(f"MULTIPLICACION: {valor1 * valor2}")
    elif opcion == 6:
        if senial < 2:
            print("ERROR. Ingresar primero los dos valores")
        else:
            print(f"DIVISION: {valor1 / valor2}")
    elif opcion >= 7:
        print("Opcion no reconocida. Ingresar nuevamente.\n")
