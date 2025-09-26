seguir = True
while seguir == True:
    distancia_km = int(input("Escriba la distancia: "))
    velocidad_kmh = int(input("Escriba la velocidad media: "))
    tiempo_horas = distancia_km / velocidad_kmh
    tiempo_dias = tiempo_horas / 24
    print(f"Tardarías {tiempo_dias} días en llegar.")
    n = str(input("Si quiere volver hacerlo pulse 's' y si quiere parar pulse 'n'"))
    if n == str("n"):
        seguir = False