"""
los números perfectos son aquellos enteros positivos iguales a la suma de sus divisores positivos, 
sin contarse el mismo número.
    ejemplo: 
    el 6, ya que 1+2+3 = 6
    
Nota: Hasta la fecha se han encontrado 51 números pefectos 
"""

# Función que determina si un numero es perdecto o no
def esPerfecto(numero):
    if numero <= 5:
        return False
    contar = []
    for n in range(1,numero):
        if numero%n == 0:
            contar.append(n)
    suma = sum(contar)
    if suma == numero:
        return True
    else:
        return False


def run():
    hasta = int(input('Ingrese el número límite (hasta) para buscar los números perfectos hasta ese número dado: '))
    lista_perfectos = []
    for n in range(5,hasta):
        if esPerfecto(n):
            lista_perfectos.append(n)

    print()
    print(lista_perfectos)
    print(f'Existen {len(lista_perfectos)} números perfectos hasta el número {hasta}.')

if __name__ == '__main__':
    run()
