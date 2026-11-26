# Ejercicio P-3: Promedio de N calificaciones y conteo de notas >= 6.0

cantidad = int(input("Ingrese la cantidad de calificaciones (N): "))

if cantidad <= 0:
    print("La cantidad de calificaciones debe ser mayor que cero.")
else:
    suma_notas = 0.0
    aprobadas = 0

    for i in range(1, cantidad + 1):
        nota = float(input(f"Ingrese la calificación {i}: "))
        suma_notas += nota
        if nota >= 6.0:
            aprobadas += 1

    promedio = suma_notas / cantidad
    print(f"Promedio aritmético: {promedio:.2f}")
    print(f"Cantidad de notas >= 6.0: {aprobadas}")
