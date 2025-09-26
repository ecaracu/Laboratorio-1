distancia = int(input("\nIntroduzca la distancia en kilometros: "))
paradas = distancia // 150000
for i in range(150000, 150000 * paradas + 1, 150000):
    print(f"Parada en el km {i}")
print(f"Total de paradas para respostar: {paradas}")