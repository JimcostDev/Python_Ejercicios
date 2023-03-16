from random import randint
import json
import time

# Inicio del tiempo de ejecución
inicio = time.time()
ruta = "./Entrada-800.txt"

# función que retorna el contenido del archivo proporcionado
def leer_archivo():
    archivo = open(ruta, "r")
    contenido = archivo.read()
    archivo.close()
    return contenido

# función que convierte una cadena de caracteres a numeros (retorna una array o lista)
def convertir_str_numero(cadena):
    # dividir la cadena en líneas separadas (se crea una lista o array)
    lineas = cadena.split("\n") 
    lista_numeros = []
    for num in range(len(lineas)):
        lista_numeros.append(int(lineas[num])) #llenar lista con numeros enteros
    return lista_numeros

# función de ordenamiento burbuja
def ordenar_burbuja(a):
  # Código método Burbuja
  for recorrido in range(len(a) - 1):  # recorridos
    for elemento in range(len(a) - 1):  # elementos del arreglo
      if a[elemento] > a[elemento + 1]:
        # cambiar de posicion los numeros (ordenar)
        t = a[elemento]
        a[elemento] = a[elemento + 1]
        a[elemento + 1] = t
  return a

# función de ordenamiento por selección
def ordenar_seleccion(a):
    # Recorrer la lista de elementos
    for num in range(len(a)):
        # Encontrar el elemento más pequeño en el resto de la lista
        min_idx = num
        for menor in range(num+1, len(a)):
            if a[menor] < a[min_idx]:
                min_idx = menor
        # Intercambiar el elemento actual con el más pequeño encontrado
        a[num], a[min_idx] = a[min_idx], a[num]
    return a


# EJECUCIÓN DEL ALGORITMO
opcion = input("""POR FAVOR ELIGE EL TIPO DE ORDENAMIENTO QUE QUIERES EJECUTAR:
1. Ordenamiento Burbuja
2. Ordenamiento por Selección

Escribe aquí tu elección: """)


cadena = leer_archivo()
array = convertir_str_numero(cadena)

try:
    opcion = int(opcion)
    if opcion == 1:
        lista_ordenada_burbuja = ordenar_burbuja(array)
        print('VER RESULTADOS POR BURBUJA: ')
        # Mostramos el arreglo ya ordenado
        print(json.dumps(lista_ordenada_burbuja, indent=4)) #utilizamos json para que se vea mejor
        # Fin del tiempo de ejecución
        fin_con_bur = time.time()
        # Duración de la ejecución
        duracion = fin_con_bur - inicio
        print("El tiempo de ejecución es:", round(duracion,2), "segundos")
    elif opcion == 2:
        lista_ordenada_seleccion = ordenar_seleccion(array)
        print('VER RESULTADOS POR SELECCIÓN: ')
        # Mostramos el arreglo ya ordenado
        print(json.dumps(lista_ordenada_seleccion, indent=4)) 
        # Fin del tiempo de ejecución
        fin_con_sel = time.time()
        duracion = fin_con_sel - inicio
        print("El tiempo de ejecución es:", round(duracion,2), "segundos")
    else:
        print('ESCOGE ENTRE 1 Y 2')
except:
    print('Solo el valido elegir numeros')







