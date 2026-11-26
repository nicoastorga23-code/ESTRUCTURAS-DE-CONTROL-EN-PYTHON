# Ejercicio P-4: Validación de clave secreta (máximo 3 intentos)

CLAVE_CORRECTA = "unisal2026"
intentos = 0
max_intentos = 3
acceso_concedido = False

while intentos < max_intentos:
    clave = input("Ingrese la clave secreta: ")
    intentos += 1

    if clave == CLAVE_CORRECTA:
        acceso_concedido = True
        break
    else:
        restantes = max_intentos - intentos
        if restantes > 0:
            print(f"Clave incorrecta. Le quedan {restantes} intento(s).")

if acceso_concedido:
    print("Acceso Concedido")
else:
    print("Cuenta Bloqueada")
