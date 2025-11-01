nombre = input("¿Cómo te llamas? ")
apellido = input("Ingrese su apellido ")

nombrecompleto = nombre + " " + apellido
# Los input siempre me retornan un str (texto)
edad = int( input("¿Cuantos años tenes? ") ) # 20

altura = 1.65
# No se puede sumar un str con un int
# Antes convertimos el formato
# edad = int( edad ) + 2

if edad > 18 :  # Si se cumple la condicion
    print("Hola ", nombrecompleto)
    print("Tu edad es", edad)
else: # Si no
    print("Sos menor de Edad, no podes ingresar")
    