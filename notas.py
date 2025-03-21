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