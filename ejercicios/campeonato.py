participantes = [
    "Liverpool", 
    "Manchester City", 
    "Leicester City",
    "Chelsea",
    "Arsenal",
]

def sorteo(participantes):
    if (len(participantes) % 2 != 0):
        participantes.append("Descansa")
        
    fixture = []
    rivales = len(participantes) - 1
    partidos = len(participantes) // 2
    
    for r in range(rivales):
        fixture.append([])
        for p in range(partidos):
            fixture[r].append((participantes[p], participantes[rivales - p]))
        participantes.insert(1, participantes.pop())
    return fixture

juegos = sorteo(participantes)

for i, juego in enumerate(juegos):
    print(f"Jornada {i+1}")
    for p in juego:
        print(f"{p[0]} vs {p[1]}")
    print()

