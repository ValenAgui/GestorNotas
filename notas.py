usuarios = []  # Lista para almacenar usuarios
notas = []  # Lista para almacenar las notas

def registrar_usuario():
    print("\n--- Registro ---")
    usuario = input("Ingrese nombre de usuario: ")
    tipo = input("Ingrese tipo (profesor/estudiante): ")
    contrasena = input("Ingrese contraseña: ")
    usuarios.append({"usuario": usuario, "tipo": tipo, "contrasena": contrasena})
    print("Usuario registrado con éxito.\n")

def login():
    print("\n--- Login ---")
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")
    for u in usuarios:
        if u["usuario"] == usuario and u["contrasena"] == contrasena:
            print("Login exitoso\n")
            return u
    print("Usuario o contraseña incorrectos.\n")
    return None

def agregar_nota():
    print("\n--- Agregar Nota ---")
    estudiante = input("Ingrese nombre del estudiante: ")
    materia = input("Ingrese la materia: ")
    nota = float(input("Ingrese la nota: "))
    notas.append({"estudiante": estudiante, "materia": materia, "nota": nota})
    print("Nota agregada con éxito.\n")

def ver_notas():
    print("\n--- Ver Notas ---")
    estudiante = input("Ingrese su nombre para ver sus notas: ")
    encontradas = [n for n in notas if n["estudiante"] == estudiante]
    if encontradas:
        for n in encontradas:
            print(f"Materia: {n['materia']}, Nota: {n['nota']}")
    else:
        print("No se encontraron notas.\n")

def menu(usuario):
    while True:
        print("\n--- Menú ---")
        print("1. Ver Notas")
        if usuario["tipo"] == "profesor":
            print("2. Agregar Nota")
        print("3. Cerrar Sesión")
        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                ver_notas()
            case "2":
                if usuario["tipo"] == "profesor":
                    agregar_nota()
            case "3":
                print("Cerrando sesión...\n")
                break
            case _:
                print("Opción inválida.\n")

def main():
    while True:
        print("\n--- Sistema de Gestión de Notas ---")
        print("1. Registrar Usuario")
        print("2. Iniciar Sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                registrar_usuario()
            case "2":
                usuario = login()
                if usuario:
                    menu(usuario)
            case "3":
                print("Saliendo...\n")
                break
            case _:
                print("Opción inválida.\n")

main()