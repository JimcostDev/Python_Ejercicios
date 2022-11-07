from random import randint, random

# creamos nuestras variables para jugar
intentos = 12
cifras = 4
jugar = True
ganar = False

# función que genera numero de n(en este caso 4) cifras (digitos) sin repetir digitos
def generar_numero_clave(digitos):
    numero_clave = [] # lista en la que guardamos el numero clave
    for i in range(digitos):
        cifra = randint(1,9)
        while cifra in numero_clave:
            cifra = randint(1,9)
        numero_clave.append(cifra)
    return numero_clave

numero_secreto = generar_numero_clave(cifras)
print(numero_secreto)


while (jugar):
    numero_del_usuario = []
    picas = 0
    fijas = 0
    numero_del_usuario = input(f'Ingresa un número de {cifras} cifras: ')
    numero = list(numero_del_usuario) #convertimos el numero del usuario a una lista
    #convertir elementos de la lista  a enteros
    for num in range(len(numero)):
        numero[num] = int(numero[num])
    intentos = intentos - 1
    if numero == numero_secreto:
        ganar = True
        jugar = False
    else:
        for n in range(cifras):
            if numero[n] in numero_secreto:
                if numero[n] == numero_secreto[n]:
                    fijas = fijas + 1
                else:
                    picas = picas + 1
        print(f'Fijas: {fijas}, Picas: {picas}. Te quedan: {intentos} intentos.')
        print()
        if intentos == 0:
            jugar = False

if ganar:
    print('ganaste')
else:
    print('perdiste') 

