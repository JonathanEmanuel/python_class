usuario = input("Ingrese el usuario: ")
clave = input("Ingrese la clave: ")
rol = input("Ingrese el rol: ")

## Para usuario admin y 123
if usuario == "admin" and clave == "123": # Si se cumple la condición
    print("Bienvenido")
  
else: # si no
    print("Usuario Invalido")


# Si es profe o secretario
if rol == "profe" or rol == "secretario":
    print("Bienvenido al Sistema")
else:
    print("Sin acceso al sistema")

# Pedir nombre y edad, y mostrar un mensaje que diga si es mayor o menor de edad.
# Y que pasa si es de 18 años
