usuarios = []  # Lista para almacenar usuarios
notas = []  # Lista para almacenar las notas

def registrar_usuario():
    print("\n--- Registro ---")
    usuario = input("Ingrese nombre de usuario: ")
    tipo = input("Ingrese tipo (profesor/estudiante): ")
    contrasena = input("Ingrese contraseña: ")
    usuarios.append({"usuario": usuario, "tipo": tipo, "contrasena": contrasena})
    print("Usuario registrado con éxito.\n")