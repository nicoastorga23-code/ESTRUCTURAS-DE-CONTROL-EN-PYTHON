# Ejercicio P-2: Calculadora de tarifas según edad

tarifa_base = float(input("Ingrese el valor de la tarifa base: "))
edad = int(input("Ingrese la edad del usuario: "))

if edad < 0:
    print("Error: la edad no puede ser negativa.")
elif edad < 5:
    descuento = 1.0
    total = 0.0
    categoria = "Menor de 5 años (Entrada gratis)"
elif edad <= 17:
    descuento = 0.50
    total = tarifa_base * (1 - descuento)
    categoria = "5 a 17 años (50% de descuento)"
elif edad <= 64:
    descuento = 0.0
    total = tarifa_base
    categoria = "18 a 64 años (Tarifa completa)"
else:
    descuento = 0.40
    total = tarifa_base * (1 - descuento)
    categoria = "Mayor de 65 años (40% de descuento)"

if edad >= 0:
    print(f"Categoría: {categoria}")
    print(f"Total a pagar: {total:.2f}")
