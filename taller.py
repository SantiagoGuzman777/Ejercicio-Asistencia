print ("ProActiva S.A.S")

# ===============================
# Sistema de Asistencia y Puntualidad
# ===============================
 
# Usuarios válidos predefinidos
usuarios_validos = {
    "admin": "1234"
}

# === INICIO DE SESIÓN ===
print("=== Iniciar sesión ===")
usuario_activo = input("Ingrese el usuario: ")
clave = input("Ingrese la contraseña: ")

if usuario_activo in usuarios_validos and usuarios_validos[usuario_activo] == clave:
    print(f"Acceso concedido. Bienvenido, {usuario_activo}.\n")
else:
    print("Usuario o contraseña incorrectos.")
    exit()

usuarios = {}   # "documento": {"nombre":..., "cargo":..., "asistencias":[(dia,hora,estado)]}
dias_validos = ["lunes", "martes", "miércoles", "jueves", "viernes"]

opcion = ""

while opcion != "7":
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Registrar nuevo usuario")
    print("2. Registrar asistencia")
    print("3. Ver historial de asistencias")
    print("4. Calcular puntualidad")
    print("5. Generar informe semanal")
    print("6. Ver base de datos completa")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\n--- Registrar usuario ---")
        nombre = input("Nombre: ")
        documento = input("Documento: ")
        cargo = input("Cargo: ")
        usuarios[documento] = {"nombre": nombre, "cargo": cargo, "asistencias": []}
        print("Usuario registrado.")

    elif opcion == "2":
        print("\n--- Registrar asistencia ---")
        documento = input("Documento del usuario: ")
        if documento in usuarios:
            dia = input("Día de la semana: ").strip().lower()
            if dia == "miercoles": 
                dia = "miércoles"

            if dia in dias_validos:
                try:
                    hora = float(input("Hora de llegada (0-24): "))
                    if 0 <= hora <= 24:
                        estado = "Puntual" if hora <= 8 else "Tarde"
                        usuarios[documento]["asistencias"].append((dia.capitalize(), hora, estado))
                        print("Asistencia registrada.")
                    else:
                        print("La hora debe estar entre 0 y 24.")
                except ValueError:
                    print("Valor inválido para la hora.")
            else:
                print("Día inválido. Solo se permiten de lunes a viernes.")
        else:
            print("Usuario no encontrado.")

    elif opcion == "3":
        print("\n--- Historial de asistencias ---")
        documento = input("Documento del usuario: ")
        if documento in usuarios:
            asistencias = usuarios[documento]["asistencias"]
            if asistencias:
                for registro in asistencias:
                    print(registro)
            else:
                print("No tiene registros.")
        else:
            print("Usuario no encontrado.")

    elif opcion == "4":
        print("\n--- Puntualidad ---")
        documento = input("Documento del usuario: ")
        if documento in usuarios:
            asistencias = usuarios[documento]["asistencias"]
            if asistencias:
                total = len(asistencias)
                puntuales = 0
                for registro in asistencias:
                    if registro[2] == "Puntual":
                        puntuales += 1
                porcentaje = (puntuales / total) * 100
                print(f"{usuarios[documento]['nombre']} -> {porcentaje:.2f}% puntualidad")
            else:
                print("No hay registros todavía.")
        else:
            print("Usuario no encontrado.")

    elif opcion == "5":
        print("\n=== Informe semanal ===")
        documento = input("Documento del usuario: ")
        if documento in usuarios:
            asistencias = usuarios[documento]["asistencias"]
            if asistencias:
                total = len(asistencias)
                puntuales = 0
                for registro in asistencias:
                    if registro[2] == "Puntual":
                        puntuales += 1
                cumplimiento = (total / 5) * 100
                puntualidad = (puntuales / total) * 100
                print(f"Empleado: {usuarios[documento]['nombre']} - {usuarios[documento]['cargo']}")
                print(f"Documento: {documento}")
                print(f"Días asistidos: {total} / 5")
                print(f"Cumplimiento: {cumplimiento:.2f}%")
                print(f"Puntualidad: {puntualidad:.2f}%")
            else:
                print("No hay registros para generar informe.")
        else:
            print("Usuario no encontrado.")

    elif opcion == "6":
        print("\n=== Base de datos completa ===")
        if usuarios:
            for documento in usuarios:
                datos = usuarios[documento]
                print(f"\nUsuario: {datos['nombre']} - {datos['cargo']}")
                print(f"Documento: {documento}")
                print("Asistencias:")
                if datos["asistencias"]:
                    for registro in datos["asistencias"]:
                        print("  ", registro)
                else:
                    print("No tiene registros.")
        else:
            print("No hay usuarios registrados.")

    elif opcion == "7":
        print("Saliendo del sistema...")

    else:
        print("Opción inválida. Intente nuevamente.")