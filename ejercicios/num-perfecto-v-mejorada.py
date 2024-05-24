def es_primo(n):
    """
    Verifica si un número es primo.
    Un número primo es aquel que solo es divisible por 1 y por sí mismo.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generar_numeros_perfectos(cantidad):
    """
    Genera una cantidad específica de números perfectos utilizando primos de Mersenne.
    Los números perfectos pares se pueden expresar como 2^(p-1) * (2^p - 1), donde
    (2^p - 1) es un número primo conocido como primo de Mersenne.
    """
    numeros_perfectos = []
    p = 2  # Iniciamos con el primer número primo
    while len(numeros_perfectos) < cantidad:
        mersenne = 2 ** p - 1  # Calculamos el número primo de Mersenne
        if es_primo(mersenne):
            numero_perfecto = 2 ** (p - 1) * mersenne  # Calculamos el número perfecto
            numeros_perfectos.append(numero_perfecto)
        p += 1  # Pasamos al siguiente número primo
    return numeros_perfectos

def run():
    """
    Función principal para ejecutar el programa.
    Solicita una cantidad de números perfectos al usuario y los encuentra.
    """
    cantidad = int(input('Ingrese la cantidad de números perfectos que desea encontrar: '))
    lista_perfectos = generar_numeros_perfectos(cantidad)
    
    print()
    print(lista_perfectos)
    print(f'Se han encontrado {len(lista_perfectos)} números perfectos.')

if __name__ == '__main__':
    run()
