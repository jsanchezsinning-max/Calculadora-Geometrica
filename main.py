print("Geometric calculator")

option = ""
pi = 3.14

while option != "1" and option != "2" and option != "3" and option != "4" and option != "5" and option != "6" and option != "7" and option != "8" and option != "10":
    print("\nMENÚ \n")
    print("1. Circulo \n2. Rectangulo \n3. Triangulo \n4. Pentagono \n5. Prisma rectangular  \n6. Esfera \n7. Cilindro \n8. Cono  \n9. Triangulo rectangulo \n10. Salir")

    option = input("\nChoose your option: ")

    if option != "1" and option != "2" and option != "3" and option != "4" and option != "5" and option != "6" and option != "7" and option != "8" and option != "10":
        print("Invalid option")

    if option == "10":
        print("Thanks for using the geometric calculator!!")
        break

    if option == "1":
            print("""\nCase 1: Circulo\n
                        1. Calcular area
                        2. Calcular radio
                        3. Calcular diametro\n""")

            circulo = (input("\nQue deseas calcular?: "))

            while circulo != "1" and circulo != "2" and circulo != "3":
                print("\nInvalid Option, Try again!")
                print("""\nCase 1: Circulo\n
                            1. Calcular area
                            2. Calcular radio
                            3. Calcular diametro\n""")
                
                circulo = (input("\nQue deseas calcular?: "))
            
            if circulo == "1":
                radio = float(input("\nIngresa el radio del circulo (en pulgadas): "))
                area = pi * (radio ** 2)
                print("\nEl area del circulo es:", area, "pulgadas²")

            elif circulo == "2":
                area = float(input("\nIngresa el area del circulo (en pulgadas²): "))
                radio = (area / pi) ** 0.5
                print("\nEl radio del circulo es:", radio, "pulgadas")

            elif circulo == "3":
                radio = float(input("\nIngresa el radio del circulo (en pulgadas): "))
                diametro = 2 * radio
                print("\nEl diametro del circulo es:", diametro, "pulgadas")
    
    elif option == "2":
            print("""\nCase 2: Rectangulo\n
                    1. Calcular base
                    2. Calcular altura
                    3. Calcular area
                    4. Calcular perimetro
                    5. Calcular diagonal\n""")

            rectangulo = (input("\nQue deseas calcular?: "))

            while rectangulo != "1" and rectangulo != "2" and rectangulo != "3" and rectangulo != "4" and rectangulo != "5":
                print("\nInvalid Option, Try again!")
                print("""\nCase 2: Rectangulo\n
                            1. Calcular base
                            2. Calcular altura
                            3. Calcular area
                            4. Calcular perimetro
                            5. Calcular diagonal\n""")
        
                rectangulo = (input("\nQue deseas calcular?: "))

            if rectangulo == "1":
                area = float(input("Ingresa el area del rectangulo (en pulgadas²): "))
                altura = float(input("Ingresa la altura del rectangulo (en pulgadas): "))
                base = area / altura
                print("La base del rectangulo es:", base, "pulgadas")

            elif rectangulo == "2":
                area = float(input("Ingresa el area del rectangulo (en pulgadas²): "))
                base = float(input("Ingresa la base del rectangulo (en pulgadas): "))
                altura = area / base
                print("La altura del rectangulo es:", altura, "pulgadas")

            elif rectangulo == "3":
                base = float(input("Ingresa la base del rectangulo (en pulgadas): "))
                altura = float(input("Ingresa la altura del rectangulo (en pulgadas): "))
                area = base * altura
                print("El area del rectangulo es:", area, "pulgadas²")

            elif rectangulo == "4":
                base = float(input("Ingresa la base del rectangulo (en pulgadas): "))
                altura = float(input("Ingresa la altura del rectangulo (en pulgadas): "))
                perimetro = 2 * (base + altura)
                print("El perimetro del rectangulo es:", perimetro, "pulgadas")

            elif rectangulo == "5":
                base = float(input("Ingresa la base del rectangulo (en pulgadas): "))
                altura = float(input("Ingresa la altura del rectangulo (en pulgadas): "))
                diagonal = (base ** 2 + altura ** 2) ** 0.5
                print("La diagonal del rectangulo es:", diagonal, "pulgadas")

    elif option == "3":
            print("""\nCase 3: Triangulo\n
                        1. Calcular area
                        2. Calcular base
                        3. Calcular altura\n""")
    
            triangulo = (input("\nQue deseas calcular?: "))

            while triangulo != "1" and triangulo != "2" and triangulo != "3":
                print("\nInvalid Option, Try again!")
                print("""\nCase 3: Triangulo\n
                            1. Calcular area
                            2. Calcular base
                            3. Calcular altura\n""")
        
            triangulo = (input("\nQue deseas calcular?: "))

            if triangulo == "1":
                base = float(input("Ingresa la base del triangulo (en pulgadas): "))
                altura = float(input("Ingresa la altura del triangulo (en pulgadas): "))
                area = (base * altura) / 2
                print("El area del triangulo es:", area, "pulgadas²")

            elif triangulo == "2":
                area = float(input("Ingresa el area del triangulo (en pulgadas²): "))
                altura = float(input("Ingresa la altura del triangulo (en pulgadas): "))
                base = (2 * area) / altura
                print("La base del triangulo es:", base, "pulgadas")

            elif triangulo == "3":
                area = float(input("Ingresa el area del triangulo (en pulgadas²): "))
                base = float(input("Ingresa la base del triangulo (en pulgadas): "))
                altura = (2 * area) / base
                print("La altura del triangulo es:", altura, "pulgadas")

    elif option == "4":
            print("""\nCase 4: Pentagono\n
                1. Calcular perimetro
                2. Calcular area
                3. Calcular apotema\n""")

            pentagono = (input("\nQue deseas calcular?: "))

            while pentagono != "1" and pentagono != "2" and pentagono != "3":
                print("\nInvalid Option, Try again!")
                print("""\nCase 4: Pentagono\n
                            1. Calcular perimetro
                            2. Calcular area
                            3. Calcular apotema\n""")
        
            pentagono = (input("\nQue deseas calcular?: "))

            if pentagono == "1":
                lado = float(input("Ingresa el lado del pentagono (en pulgadas): "))
                perimetro = 5 * lado
                print("El perimetro del pentagono es:", perimetro, "pulgadas")

            elif pentagono == "2":
                perimetro = float(input("Ingresa el perimetro del pentagono (en pulgadas): "))
                apotema = float(input("Ingresa la apotema del pentagono (en pulgadas): "))
                area = (perimetro * apotema) / 2
                print("El area del pentagono es:", area, "pulgadas²")

            elif pentagono == "3":
                area = float(input("Ingresa el area del pentagono (en pulgadas²): "))
                perimetro = float(input("Ingresa el perimetro del pentagono (en pulgadas): "))
                apotema = (2 * area) / perimetro
                print("La apotema del pentagono es:", apotema, "pulgadas")

    elif option == "5":
            print("""\nCase 5: Prisma rectangular\n
                        1. Calcular volumen
                        2. Calcular largo
                        3. Calcular ancho
                        4. Calcular altura\n""")

            prisma = input("\nQue deseas calcular?: ")

            while prisma != "1" and prisma != "2" and prisma != "3" and prisma != "4":
                print("\nInvalid Option, Try again!")
                print("""\nCase 5: Prisma rectangular\n
                            1. Calcular volumen
                            2. Calcular largo
                            3. Calcular ancho
                            4. Calcular altura\n""")
        
            prisma = input("\nQue deseas calcular?: ")

            if prisma == "1":
                largo = float(input("Ingresa el largo del prisma (en pulgadas): "))
                ancho = float(input("Ingresa el ancho del prisma (en pulgadas): "))
                altura = float(input("Ingresa la altura del prisma (en pulgadas): "))
                volumen = largo * ancho * altura
                print("El volumen del prisma es:", volumen, "pulgadas³")

            elif prisma == "2":
                volumen = float(input("Ingresa el volumen del prisma (en pulgadas³): "))
                ancho = float(input("Ingresa el ancho del prisma (en pulgadas): "))
                altura = float(input("Ingresa la altura del prisma (en pulgadas): "))
                largo = volumen / (ancho * altura)
                print("El largo del prisma es:", largo, "pulgadas")

            elif prisma == "3":
                volumen = float(input("Ingresa el volumen del prisma (en pulgadas³): "))
                largo = float(input("Ingresa el largo del prisma (en pulgadas): "))
                altura = float(input("Ingresa la altura del prisma (en pulgadas): "))
                ancho = volumen / (largo * altura)
                print("El ancho del prisma es:", ancho, "pulgadas")

            elif prisma == "4":
                volumen = float(input("Ingresa el volumen del prisma (en pulgadas³): "))
                largo = float(input("Ingresa el largo del prisma (en pulgadas): "))
                ancho = float(input("Ingresa el ancho del prisma (en pulgadas): "))
                altura = volumen / (largo * ancho)
                print("La altura del prisma es:", altura, "pulgadas")

    elif option == "6":
            print("""\nCase 6: Esfera\n
                        1. Calcular volumen
                        2. Calcular radio\n""")

            esfera = input("Que deseas calcular?: ")

            while esfera != "1" and esfera != "2":
                print("\nInvalid Option, Try again!")
                print("""\nCase 6: Esfera\n
                            1. Calcular volumen
                            2. Calcular radio\n""")
        
                esfera = input("Que deseas calcular?: ")

            if esfera == "1":
                radio = float(input("Ingresa el radio de la esfera (en pulgadas): "))

                if radio < 0:
                        print("Error: el radio no puede ser negativo")
                else:
                    volumen = (4/3) * pi * (radio ** 3)
                    print("El volumen de la esfera es:", volumen, "pulgadas³")

            elif esfera == "2":
                volumen = float(input("Ingresa el volumen de la esfera (en pulgadas³): "))

                if volumen < 0:
                    print("Error: el volumen no puede ser negativo")
                else:
                    radio = (volumen / ((4/3) * pi)) ** (1/3)
                    print("El radio de la esfera es:", radio, "pulgadas")

    elif option == "7":
            print("""\nCase 7: Cilindro\n
                        1. Calcular volumen
                        2. Calcular radio
                        3. Calcular altura\n""")

            cilindro = input("Que deseas calcular?: ")

            while cilindro != "1" and cilindro != "2" and cilindro != "3":
                print("\nInvalid Option, Try again!")
                print("""\nCase 7: Cilindro\n
                            1. Calcular volumen
                            2. Calcular radio
                            3. Calcular altura\n""")
        
                cilindro = input("Que deseas calcular?: ")

            if cilindro == "1":
                radio = float(input("Ingresa el radio del cilindro (en pulgadas): "))
                altura = float(input("Ingresa la altura del cilindro (en pulgadas): "))

                if radio < 0 or altura < 0:
                    print("Error: los valores no pueden ser negativos")
                else:
                    volumen = pi * (radio ** 2) * altura
                    print("El volumen del cilindro es:", volumen, "pulgadas³")

            elif cilindro == "2":
                volumen = float(input("Ingresa el volumen del cilindro (en pulgadas³): "))
                altura = float(input("Ingresa la altura del cilindro (en pulgadas): "))

                if altura == 0:
                    print("Error: no se puede dividir por 0")
                else:
                    radio = (volumen / (pi * altura)) ** 0.5
                    print("El radio del cilindro es:", radio, "pulgadas")

            elif cilindro == "3":
                volumen = float(input("Ingresa el volumen del cilindro (en pulgadas³): "))
                radio = float(input("Ingresa el radio del cilindro (en pulgadas): "))

                if radio == 0:
                    print("Error: no se puede dividir por 0")
                else:
                    altura = volumen / (pi * (radio ** 2))
                    print("La altura del cilindro es:", altura, "pulgadas")

    elif option == "8":
            print("""\nCase 8: Cono\n
                        1. Calcular volumen
                        2. Calcular radio
                        3. Calcular altura\n""")

            cono = input("Que deseas calcular?: ")

            while cono != "1" and cono != "2" and cono != "3":
                print("\nInvalid Option, Try again!")
                print("""\nCase 8: Cono\n
                            1. Calcular volumen
                            2. Calcular radio
                            3. Calcular altura\n""")

                cono = input("Que deseas calcular?: ")

            if cono == "1":
                radio = float(input("Ingresa el radio del cono (en pulgadas): "))
                altura = float(input("Ingresa la altura del cono (en pulgadas): "))

                if radio < 0 or altura < 0:
                    print("Error: los valores no pueden ser negativos")
                else:
                    volumen = (1/3) * pi * (radio ** 2) * altura
                    print("El volumen del cono es:", volumen, "pulgadas³")

            elif cono == "2":
                volumen = float(input("Ingresa el volumen del cono (en pulgadas³): "))
                altura = float(input("Ingresa la altura del cono (en pulgadas): "))

                if altura == 0:
                    print("Error: no se puede dividir por 0")
                else:
                    radio = ((3 * volumen) / (pi * altura)) ** 0.5
                    print("El radio del cono es:", radio, "pulgadas")

            elif cono == "3":
                volumen = float(input("Ingresa el volumen del cono (en pulgadas³): "))
                radio = float(input("Ingresa el radio del cono (en pulgadas): "))

                if radio == 0:
                    print("Error: no se puede dividir por 0")
                else:
                    altura = (3 * volumen) / (pi * (radio ** 2))
                    print("La altura del cono es:", altura, "pulgadas")

    elif option == "9":
            print("""\nCase 9: Triangulo rectangulo\n
                        1. Calcular hipotenusa
                        2. Calcular cateto 1
                        3. Calcular cateto 2\n""")

            triangulo_r = input("Que deseas calcular?: ")

            while triangulo_r != "1" and triangulo_r != "2" and triangulo_r != "3":
                print("\nInvalid Option, Try again!")
                print("""\nCase 9: Triangulo rectangulo\n
                            1. Calcular hipotenusa
                            2. Calcular cateto 1
                            3. Calcular cateto 2\n""")

                triangulo_r = input("Que deseas calcular?: ")

            if triangulo_r == "1":
                cateto1 = float(input("Ingresa el cateto 1 (en pulgadas): "))
                cateto2 = float(input("Ingresa el cateto 2 (en pulgadas): "))

                if cateto1 < 0 or cateto2 < 0:
                    print("Error: los valores no pueden ser negativos")
                else:
                    hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** 0.5
                    print("La hipotenusa es:", hipotenusa, "pulgadas")

            elif triangulo_r == "2":
                hipotenusa = float(input("Ingresa la hipotenusa (en pulgadas): "))
                cateto2 = float(input("Ingresa el cateto 2 (en pulgadas): "))

                if hipotenusa <= cateto2:
                    print("Error: la hipotenusa debe ser mayor que el cateto")
                else:
                    cateto1 = (hipotenusa ** 2 - cateto2 ** 2) ** 0.5
                    print("El cateto 1 es:", cateto1, "pulgadas")

            elif triangulo_r == "3":
                hipotenusa = float(input("Ingresa la hipotenusa (en pulgadas): "))
                cateto1 = float(input("Ingresa el cateto 1 (en pulgadas): "))

                if hipotenusa <= cateto1:
                    print("Error: la hipotenusa debe ser mayor que el cateto")
                else:
                    cateto2 = (hipotenusa ** 2 - cateto1 ** 2) ** 0.5
                    print("El cateto 2 es:", cateto2, "pulgadas")
