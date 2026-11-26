# Ejercicio P-1: Mayor de tres números enteros

a = int(input("Ingrese el primer número entero: "))
b = int(input("Ingrese el segundo número entero: "))
c = int(input("Ingrese el tercer número entero: "))

if a == b == c:
    print("Todos los números ingresados son iguales.")
elif a >= b and a >= c:
    print(f"El número mayor es: {a}")
elif b >= a and b >= c:
    print(f"El número mayor es: {b}")
else:
    print(f"El número mayor es: {c}")
