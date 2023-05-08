import time
import datetime

# simulación de un reloj
H = 0 # Horas
M = 0 # Minutos
S = 0 # Segundos

while True:
    # aumentar segundos cada segundo
    S += 1
    # las instrucciones 'assert'  verifican que los valores de H,M,S sean siempre menores que 24, 60 y 60, respectivamente:
    assert S < 60
    time.sleep(1)
    if (S == 60):
        S = 0
        M += 1
        assert M < 60
    if (M == 60):
        M = 0
        H += 1
        assert H < 24
    if (H == 24):
        H = 0
    # formatear la hora
    hora_formateada = datetime.datetime(1, 1, 1, H, M, S).strftime("%H:%M:%S")
    print(hora_formateada, end="", flush=True)  
    print("\r", end="", flush=True)


