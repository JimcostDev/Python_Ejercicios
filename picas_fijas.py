from random import randint

intentos = 0
unidades = 4
jugar = True
ganar = False
picas = 0
fijas = 0

# funcion que genera numero random
def obtenerNumeroRandom(cantidadCifras):
    vectorNumeroSecreto = []
    for i in range(cantidadCifras):
        cifra = randint(0, 9)
        while cifra in vectorNumeroSecreto:
            cifra = randint(0, 9)
        vectorNumeroSecreto.append(cifra)
    return vectorNumeroSecreto

numeroRandom = obtenerNumeroRandom(unidades)
print(numeroRandom)

# funcion que retorna picas y fijas
def retornarFijasPicas(x):
    global fijas, picas
    fijas = 0
    picas = 0
    for n in range(unidades):
        if x[n] in numeroRandom:
            if x[n] == numeroRandom[n]:
                fijas = fijas + 1
            else:
                picas = picas + 1
    print(f'Fijas: {fijas}, Picas: {picas}. Llevas: {intentos} intentos.')

while jugar:
    numeroUsuario = input(f'Ingresa un número de {unidades} unidades: ')
    cantidad_unidades = len(numeroUsuario)
    if cantidad_unidades == 4:
        numero = list(numeroUsuario)
        numero = [int(num) for num in numero] # convertir lista string a int
        intentos = intentos + 1

        if numero == numeroRandom:
            ganar = True
            jugar = False
        else:
            retornarFijasPicas(numero)
            if intentos == 12:
                print('Perdiste')
                jugar = False
    else:
        print('Debe ser un número de 4 unidades')
        intentos = intentos + 1

# funcion para mostrar mensajes
def MensajeSalida():
    mensajes = [
        "Excelente, ganaste, lo hiciste en {} intentos",
        "Muy bien, ganaste, lo hiciste en {} intentos",
        "Bien, estás progresando, ganaste, lo hiciste en {} intentos",
        "Regular, ganaste, lo hiciste en {} intentos",
        "Mal, pero ganaste, lo hiciste en {} intentos"
    ]
    
    if ganar:
        if intentos <= 2:
            mensaje_index = 0
        elif intentos <= 4:
            mensaje_index = 1
        elif intentos <= 8:
            mensaje_index = 2
        elif intentos <= 10:
            mensaje_index = 3
        else:
            mensaje_index = 4
        
        mensaje = mensajes[mensaje_index]
        print(mensaje.format(intentos))

MensajeSalida()
