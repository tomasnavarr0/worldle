print("Escribí una palabra maestro (--En minúscula porfa, en serio, que si no se rompe xD)  ")
palabra = "fceia"
tablero = []
ganar = False
contadorJuego = 0

colors = {
    'verde': '\033[92m',
    'amarillo': '\033[93m',
    'rojo': '\033[91m',
    'ENDC': '\033[0m'
}


# def colorLetra(letra, color):
def colorLetra(letra, color):
    return colors[color] + letra + colors['ENDC']


# Iniciar el tablerito
for i in range(5):
    tablero.append(["_" for l in range(5)])

# ----------------------------------------

while (not ganar) and contadorJuego < len(palabra):
    texto = input("")
    while len(texto) != len(palabra):
        print(f"La palabra tiene que tener 5 letras...")
        texto = input("")

    # ------------GANAR------------------
    if palabra == texto:
        tablero[contadorJuego] = [l for l in texto]
        ganar == True
        print("---Felicitaciones, ganaste el juego---")

    # --------------Letra en la palabra--------------
    else:
        testeo = []
        for j in range(len(texto)):

            if texto[j] == palabra[j]:
                testeo.append(texto[j], 'verde')

            elif texto[j] in palabra:
                testeo.append(colorLetra(texto[j], 'amarillo'))

            else:
                testeo.append(colorLetra(texto[j], 'rojo'))

        tablero[contadorJuego] = testeo

    # Dibujo
    for i in range(5):
        print(" ".join(tablero[i]))

    contadorJuego += 1
