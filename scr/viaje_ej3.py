edad = int(input("\nIntroduzca su edad: "))
fisico = 0
while fisico > 10 or fisico < 1:
    fisico = int(input("Introduzca su nivel físico del 1 al 10: "))
if edad < 18:
    print("Debes ser mayor de edad")
elif fisico < 5:
    print("Debes estar en mejor forma")
else:
    print("¡Listo para despegar!")