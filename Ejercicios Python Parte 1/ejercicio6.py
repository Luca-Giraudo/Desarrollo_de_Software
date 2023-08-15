"""Asado"""
cantInvitados = int(input("Ingresar la cantidad de invitados: "))
precioCarne = float(input("Ingresar el precio del kg de carne: "))
cantCarne = 0.7 * cantInvitados
costo = cantCarne * precioCarne
print(f"La cantidad de carne que debe comprar es {cantCarne} y el total a pagar es {costo}")