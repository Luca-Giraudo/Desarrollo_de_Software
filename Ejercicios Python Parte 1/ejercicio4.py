"""Descuento en el supermercado"""
monto = int(input("Ingresar el monto de la compra: "))
if monto > 3500:
    importe = monto - (monto * 0.10)
else:
    importe = monto
print(f"El importe a pagar es {importe}")