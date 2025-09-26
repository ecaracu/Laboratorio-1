seguir = True
while seguir == True:
    distancia_km = int(input("Escriba la distancia: "))
    velocidad_kmh = int(input("Escriba la velocidad media: "))
    tiempo_horas = distancia_km // velocidad_kmh
    tiempo_semana = tiempo_horas // 168
    dias_sobrantes = tiempo_horas % 168
    print(f"Tardarías {tiempo_semana} semanas y {dias_sobrantes} dias en llegar.")
    n = str(input("Si quiere volver hacerlo pulse 's' y si quiere parar pulse 'n'"))
    if n == str("n"):
        seguir = False