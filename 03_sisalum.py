# ============================================================
# SISTEMA DE GESTIÓN DE ESTUDIANTES
# ============================================================

NOTA_APROBACION = 60
NOTA_MAXIMA = 100


def calcular_promedio(notas):
    """
    Calcula el promedio de las notas de un estudiante.
    """
    if len(notas) == 0:
        return 0

    suma = 0

    # [CORREGIDO] Se quitó '- 1' para incluir la última nota del estudiante
    for i in range(len(notas)):
        suma = suma + notas[i]

    promedio = suma / len(notas)
    return promedio


def determinar_estado(promedio):
    """
    Determina si un estudiante está aprobado o reprobado.
    """
    # [CORREGIDO] Se cambió '>' por '>=' para que el 60 sea aprobado
    if promedio >= NOTA_APROBACION:
        return "APROBADO"
    else:
        return "REPROBADO"


def obtener_nota_mayor(notas):
    if len(notas) == 0:
        return 0

    # [CORREGIDO] Inicializar con la primera nota y usar '>'
    mayor = notas[0]

    for nota in notas:
        if nota > mayor:
            mayor = nota

    return mayor


def obtener_nota_menor(notas):
    if len(notas) == 0:
        return 0

    # [CORREGIDO] Inicializar con la primera nota y usar '<'
    menor = notas[0]

    for nota in notas:
        if nota < menor:
            menor = nota

    return menor


def registrar_estudiante(estudiantes):
    print("\n===== REGISTRO DE ESTUDIANTE =====")

    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    cedula = input("Cédula: ")

    notas = []

    cantidad = int(input("¿Cuántas notas desea ingresar?: "))

    for i in range(cantidad):
        nota = float(input("Ingrese la nota " + str(i + 1) + ": "))

        # [CORREGIDO] Se cambió 'or' por 'and' para validar el rango [0, NOTA_MAXIMA]
        if nota >= 0 and nota <= NOTA_MAXIMA:
            notas.append(nota)
        else:
            print("Nota inválida.")

    estudiante = {
        "cedula": cedula,
        "nombre": nombre,
        "apellido": apellido,
        "notas": notas
    }

    estudiantes.append(estudiante)
    print("Estudiante registrado correctamente.")


def buscar_estudiante(estudiantes, cedula):
    for estudiante in estudiantes:
        if estudiante["cedula"] == cedula:
            return estudiante

    # [CORREGIDO] 'return None' estaba indentado dentro del bucle 'for', cortando la búsqueda en el primer alumno
    return None


def mostrar_estudiante(estudiante):
    promedio = calcular_promedio(estudiante["notas"])
    estado = determinar_estado(promedio)
    mayor = obtener_nota_mayor(estudiante["notas"])
    menor = obtener_nota_menor(estudiante["notas"])

    print("\n===================================")
    print("DATOS DEL ESTUDIANTE")
    print("===================================")
    print("Cédula:", estudiante["cedula"])
    print("Nombre:", estudiante["nombre"])
    print("Apellido:", estudiante["apellido"])
    print("Notas:", estudiante["notas"])
    print("Promedio:", round(promedio, 2))
    print("Nota mayor:", mayor)
    print("Nota menor:", menor)
    print("Estado:", estado)
    print("===================================")


def calcular_promedio_general(estudiantes):
    if len(estudiantes) == 0:
        return 0

    suma_promedios = 0

    # [CORREGIDO] Antes dividía la suma de promedios entre la cantidad total de notas en vez de la cantidad de estudiantes
    for estudiante in estudiantes:
        promedio = calcular_promedio(estudiante["notas"])
        suma_promedios = suma_promedios + promedio

    return suma_promedios / len(estudiantes)


def contar_estados(estudiantes):
    aprobados = 0
    reprobados = 0

    for estudiante in estudiantes:
        promedio = calcular_promedio(estudiante["notas"])

        if promedio >= NOTA_APROBACION:
            aprobados = aprobados + 1
        else:
            reprobados = reprobados + 1

    return aprobados, reprobados


def obtener_mejor_estudiante(estudiantes):
    # [CORREGIDO] Inicializar con el primer estudiante y buscar promedio MAYOR ('>')
    mejor_estudiante = estudiantes[0]
    mejor_promedio = calcular_promedio(mejor_estudiante["notas"])

    for estudiante in estudiantes:
        promedio = calcular_promedio(estudiante["notas"])

        if promedio > mejor_promedio:
            mejor_promedio = promedio
            mejor_estudiante = estudiante

    return mejor_estudiante


def obtener_peor_estudiante(estudiantes):
    # [CORREGIDO] Inicializar con el primer estudiante y buscar promedio MENOR ('<')
    peor_estudiante = estudiantes[0]
    peor_promedio = calcular_promedio(peor_estudiante["notas"])

    for estudiante in estudiantes:
        promedio = calcular_promedio(estudiante["notas"])

        if promedio < peor_promedio:
            peor_promedio = promedio
            peor_estudiante = estudiante

    return peor_estudiante


def mostrar_estadisticas(estudiantes):
    print("\n===================================")
    print("ESTADÍSTICAS DEL CURSO")
    print("===================================")

    if len(estudiantes) == 0:
        print("No existen estudiantes registrados.")
        return

    promedio_general = calcular_promedio_general(estudiantes)
    aprobados, reprobados = contar_estados(estudiantes)
    mejor = obtener_mejor_estudiante(estudiantes)
    peor = obtener_peor_estudiante(estudiantes)

    print("Cantidad de estudiantes:", len(estudiantes))
    print("Promedio general:", round(promedio_general, 2))
    print("Aprobados:", aprobados)
    print("Reprobados:", reprobados)

    if mejor is not None:
        print("Mejor estudiante:", mejor["nombre"], mejor["apellido"])

    if peor is not None:
        print("Peor estudiante:", peor["nombre"], peor["apellido"])

    print("===================================")


def mostrar_todos(estudiantes):
    print("\n===================================")
    print("LISTADO DE ESTUDIANTES")
    print("===================================")

    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
        return

    for estudiante in estudiantes:
        promedio = calcular_promedio(estudiante["notas"])
        print(
            estudiante["cedula"],
            "-",
            estudiante["nombre"],
            estudiante["apellido"],
            "- Promedio:",
            round(promedio, 2)
        )


def menu():
    estudiantes = []

    while True:
        print("\n")
        print("===================================")
        print(" SISTEMA DE GESTIÓN ACADÉMICA")
        print("===================================")
        print("1. Registrar estudiante")
        print("2. Buscar estudiante")
        print("3. Mostrar todos")
        print("4. Mostrar estadísticas")
        print("5. Salir")
        print("===================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_estudiante(estudiantes)
        elif opcion == "2":
            cedula = input("Ingrese la cédula a buscar: ")
            estudiante = buscar_estudiante(estudiantes, cedula)
            if estudiante:
                mostrar_estudiante(estudiante)
            else:
                print("Estudiante no encontrado.")
        elif opcion == "3":
            mostrar_todos(estudiantes)
        elif opcion == "4":
            mostrar_estadisticas(estudiantes)
        elif opcion == "5":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida.")


# ============================================================
# INICIO DEL PROGRAMA
# ============================================================

menu()
