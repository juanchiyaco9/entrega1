import random
words = ["python","programa","variable","funcion","bucle","cadena","entero","lista",] 

word = random.choice(words)
guessed = []
attempts = 6
puntaje = 0 

print("¡Bienvenido al Ahorcado!")
print()

while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        puntaje +=6 #Ganó. Son 6 puntos
        print("¡Ganaste!")
        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ")
    ## Punto 1. Validar datos
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    if len(letter) != 1 or letter.lower() not in alfabeto:
        print("Entrada no válida")
        print()
        continue

    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        puntaje -= 1 #Erró.Resta 1.
        print("Esa letra no está en la palabra.")

    print()
else:
    print(f"¡Perdiste! La palabra era: {word}")
    puntaje =  0 #Perdió. 0 puntos

print(f"Tu puntaje fue: {puntaje}") #Imprime puntaje