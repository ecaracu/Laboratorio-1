distancia_km = int(input("Escriba la distancia: "))
velocidad_kmh = int(input("Escriba la velocidad media: "))
tiempo_horas = distancia_km / velocidad_kmh
tiempo_dias = tiempo_horas / 24
print(f"Tardarías {tiempo_dias} días en llegar.")