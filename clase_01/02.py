usuario = input("Ingrese el usuario: ")
clave = input("Ingrese la clave: ")

## Para usuario admin y 123
if usuario == "admin":
    if clave == "123":
        print("Bienvenido")
    else:
        print("Clave Invalida")
else:
    print("Usuario Invalido")
