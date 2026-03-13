print("Geometric calculator")

option = 0

while option != 10:
    print("\nMENÚ \n")
    print("1. Circulo \n2. Rectangulo \n3. Triangulo \n4. Pentagono \n5. Prisma rectangular  \n6. Esfera \n7. Cilindro \n8. Cono  \n9. Triangulo rectangulo \n10. Salir")
    option = int(input("\nChoose your option: "))

    if option == 10:
        break

    if option == 1:
        print("""Case 1: Circulo
            1. Calcular area
            2. Calcular radio\n""")
        circulo = int(input("Que deseas calcular?: "))
        
        