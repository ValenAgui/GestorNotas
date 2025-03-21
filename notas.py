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