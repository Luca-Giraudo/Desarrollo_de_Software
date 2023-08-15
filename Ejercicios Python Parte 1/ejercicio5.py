"""Club deportivo"""
socioNombre = input("Ingresar el nombre del socio: ")
socioEdad = int(input("Ingresar la edad del socio: "))
if 13 <= socioEdad < 15:
    print(f"El socio {socioNombre} pertenece a la categoria infantiles")
if 15 <= socioEdad < 17:
     print(f"El socio {socioNombre} pertenece a la categoria cadetes")
if 17 <= socioEdad < 19:
     print(f"El socio {socioNombre} pertenece a la categoria juveniles")
if 19 <= socioEdad:
     print(f"El socio {socioNombre} pertenece a la categoria mayores")