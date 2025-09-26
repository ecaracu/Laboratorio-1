distancia = 225000000
for i in range(10000, 50001, 10000):
    horas = distancia / i
    dias = horas / 24
    print(f"Velocidad {i} km/h --> Tiempo: {dias} días")