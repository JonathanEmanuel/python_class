# Clase 01 - Fundamentos de Python y Repaso General

## [Temario](../README.md)
Conceptos fundamentales de Python, variables, tipos de datos básicos, entrada y salida de datos, y condicionales simples.

Python es un lenguaje simple, ideal para principiantes. 

**Variables y tipos de datos** 
- Las variables almacenan información.
- En Python no es necesario declarar el tipo explícitamente (es de tipado dinámico).

``` py
    nombre = "Julieta"
    edad = 25
    altura = 1.65

    print(nombre)
    print("Edad:", edad)
    print("Altura:", altura)
```

**Entrada de datos con input()** 
- input() siempre devuelve un string.
- Hay que convertirlo si queremos usarlo como número.

``` py
    nombre = input("¿Cómo te llamas? ")
    edad = int(input("¿Cuántos años tenes? "))

    print("Hola", nombre)
    print("El proximo año vas a tener", edad + 1)
```

**Condicionales simples con if**
- Las estructuras condicionales las suamos para que el programa tome decisiones.
``` py
    edad = int(input("¿Cuantos años tenes? "))

    if edad > 18:
        print("Sos mayor de edad")
    else:
        print("Sos menor de edad.")
```

**Operadores Lógicos**

---

- [Ejemplo 1](01.py)
- [Ejemplo 2](02.py)
- [Ejemplo 2](03.py)

