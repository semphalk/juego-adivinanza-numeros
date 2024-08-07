import random

def juego_adininanza():
    numero_secreto = random.randint(1,100)
    intentos = 0
    adivinado = False
    print("Adivinar número!")
    while not adivinado:
        adivinanza = input("Introduzca un número del 1 al 100:")
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)
            intentos += 1
            if adivinanza < numero_secreto:
                print(f"Nro es > a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"Nro. es < a {adivinanza}")
            else:
                print(f"Acertaste en {intentos} intentos!")
                break
        else:
            print("Ingresar nro. entre 1 y 100!")

juego_adininanza()