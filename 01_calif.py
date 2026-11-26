# ============================================
# SISTEMA DE CONTROL DE CALIFICACIONES
# ============================================

def calcular_promedio(notas):
    # [CORREGIDO] Validar lista vacía para evitar división por cero (ZeroDivisionError)
    if len(notas) == 0:
        return 0

    total = 0
    # [CORREGIDO] Antes tenía range(0, len(notas) - 1), lo que ignoraba la última nota
    for nota in notas:
        total = total + nota

    promedio = total / len(notas)
    return promedio


def obtener_mayor(notas):
    if len(notas) == 0:
        return 0

    # [CORREGIDO] Inicializar con el primer elemento en lugar de 0
    mayor = notas[0]

    for nota in notas:
        # [CORREGIDO] Antes usaba '<', lo que buscaba el menor en vez del mayor
        if nota > mayor:
            mayor = nota

    return mayor


def obtener_menor(notas):
    if len(notas) == 0:
        return 0

    # [CORREGIDO] Inicializar con el primer elemento; antes era 0 y nunca cambiaba
    menor = notas[0]

    for nota in notas:
        # [CORREGIDO] Antes usaba '>', lo que buscaba el mayor en vez del menor
        if nota < menor:
            menor = nota

    return menor


def contar_aprobados(notas):
    aprobados = 0

    for nota in notas:
        # [CORREGIDO] Se cambió '>' por '>=' para incluir el 60 como nota aprobatoria
        if nota >= 60:
            aprobados = aprobados + 1

    return aprobados


def calcular_porcentaje_aprobados(notas):
    if len(notas) == 0:
        return 0

    aprobados = contar_aprobados(notas)
    porcentaje = (aprobados / len(notas)) * 100
    return porcentaje


def mostrar_resultados(nombre, notas):
    promedio = calcular_promedio(notas)
    mayor = obtener_mayor(notas)
    menor = obtener_menor(notas)
    aprobados = contar_aprobados(notas)
    porcentaje = calcular_porcentaje_aprobados(notas)

    print("================================")
    print("Alumno:", nombre)
    print("Notas:", notas)
    print("Promedio:", round(promedio, 2))
    print("Nota mayor:", mayor)
    print("Nota menor:", menor)
    print("Aprobados:", aprobados)
    print("Porcentaje de aprobados:", round(porcentaje, 2), "%")
    print("================================")


# Programa principal
nombre = input("Ingrese el nombre del alumno: ")
cantidad = int(input("Ingrese la cantidad de notas: "))

notas = []

for i in range(cantidad):
    # [CORREGIDO] Se muestra i + 1 al usuario para numerar desde 1 en lugar de 0
    nota = int(input("Ingrese la nota " + str(i + 1) + ": "))

    # [CORREGIDO] Se cambió 'or' por 'and' para exigir que esté dentro del rango [0, 100]
    if nota >= 0 and nota <= 100:
        notas.append(nota)
    else:
        print("La nota debe estar entre 0 y 100")

mostrar_resultados(nombre, notas)

# [CORREGIDO] Se calcula 'promedio' en el ámbito global; antes daba NameError
promedio = calcular_promedio(notas)

if promedio >= 60:
    print("El alumno está APROBADO")
else:
    print("El alumno está REPROBADO")
