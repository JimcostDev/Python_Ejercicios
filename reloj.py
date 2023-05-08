import time
import datetime

# simulación de un reloj
H = 0 # Horas
M = 0 # Minutos
S = 0 # Segundos

while True:
    # aumentar segundos cada segundo
    S += 1
    time.sleep(0.1)
    if (S == 60):
        S = 0
        M += 1
    if (M == 60):
        S = 0
        M = 0
        H += 1
    if (H == 24):
        S = 0
        M = 0
        H = 0
    # formatear la hora
    hora_formateada = datetime.datetime(1, 1, 1, H, M, S).strftime("%H:%M:%S")
    print(hora_formateada, end="", flush=True)  
    print("\r", end="", flush=True)


