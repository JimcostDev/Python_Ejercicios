import math

# mis variables
numero = 50.66;
print("El número es: ", numero);
parte_fraccionaria, parte_entera = math.modf(numero);
num_decimal = int(parte_entera); 


# estas variables son para calcular la parte en fraccion
dobles = [];
dobles.append(parte_fraccionaria);
lista_fracciones = [];
lista_binaria = [];

def convertirABinarioParteFraccionaria():
    for i in range(64):
        valor = dobles[i] * 2;
        dobles.append(valor);
        # separo los decimales de las partes enteras
        p_fraccion, p_entera = math.modf(dobles[i]);
        p_fraccion = round(p_fraccion,2); # redondeo el numero a 2 decimales
        lista_fracciones.append(p_fraccion);
        frac, ent = math.modf(lista_fracciones[i]);
        lista_binaria.append(frac*2);
        if(lista_fracciones[i] == 0.0):
            break;

    #lleno el arrray(lista) con cada parte decimal para formar el binario(b)
    resultado = []
    for b in lista_binaria:
        resultado.append(int(b));

    #convertir lista a str
    cadena = str(resultado);
    numero_sin_comas = cadena.replace(',', '');
    return numero_sin_comas;


# función que convierte de binario a decimal
def binarioADecimal(binario):
    bi_de = int(binario);
    return bi_de;

#función que convierte decimal a binario
def decimalABinario(decimal):
    de_bi = bin(decimal);
    return de_bi;

resultado_decimal_bin = decimalABinario(num_decimal)
print(f'El numero decimal: {num_decimal} a binario es = {resultado_decimal_bin[2:]}');
print(f'su parte fraccionaria en binario es = {convertirABinarioParteFraccionaria()}');
print()

# partes dobles 
print('PARTES DOBLES, PASO A PASO')
print(lista_fracciones);


"""
descomentar el codigo de abajo si queremos mostar la conversion de binario a decimal (solo partes enteras), 
siempre inicia con 0b y despues va el binario
"""
# num_binario = 0b111101; # aqui colocamos un numero binario si queremos convertirlo a decimal
# print(f'El numero binario: {bin(num_binario)} a decimal es = {binarioADecimal(num_binario)}');
