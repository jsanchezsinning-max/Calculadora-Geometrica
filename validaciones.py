print("Geometric calculator")

option = ""
pi = 3.14

while option != "1" and option != "2" and option != "3" and option != "4" and option != "5" and option != "6" and option != "7" and option != "8" and option != "10":
    print("\nMENÚ \n")
    print("1. Circulo \n2. Rectangulo \n3. Triangulo \n4. Pentagono \n5. Prisma rectangular  \n6. Esfera \n7. Cilindro \n8. Cono  \n9. Triangulo rectangulo \n10. Salir")

    option = input("\nChoose your option (Numero entero): ")

    if option != "1" and option != "2" and option != "3" and option != "4" and option != "5" and option != "6" and option != "7" and option != "8" and option != "10":
        print("Invalid option")

    if option == "10":
        print("Thanks for using thegeometric calculator!!")
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
                radio = float(input("\nIngresa el radio del circulo (numero entero): "))
                area = pi * (radio ** 2)
                print("\nEl area del circulo es: ", area)

            elif circulo == "2":
                area = float(input("\nIngresa el area del circulo (numero entero): "))
                radio = (area / pi) ** 0.5
                print("\nEl radio del circulo es: ", radio)

            elif circulo == "3":
                radio = float(input("\nIngresa el radio del circulo (numero entero): "))
                diametro = 2 * radio
                print("\nEl diametro del circulo es: ", diametro)
    
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
                area = float(input("Ingresa el area del rectangulo (numero entero): "))
                altura = float(input("Ingresa la altura del rectangulo (numero entero): "))
                base = area / altura
                print("La base del rectangulo es: ", base)

            elif rectangulo == "2":
                area = float(input("Ingresa el area del rectangulo (numero entero): "))
                base = float(input("Ingresa la base del rectangulo (numero entero): "))
                altura = area / base
                print("La altura del rectangulo es: ", altura)

            elif rectangulo == "3":
                base = float(input("Ingresa el base del rectangulo (numero entero): "))
                altura = float(input("Ingresa la altura del rectangulo (numero entero): "))
                area = base * altura
                print("El area del rectangulo es: ", area)

            elif rectangulo == "4":
                base = float(input("Ingresa el base del rectangulo (numero entero): "))
                altura = float(input("Ingresa la altura del rectangulo (numero entero): "))
                perimetro = 2 * (base + altura)
                print("El perimetro del rectangulo es: ", perimetro)

            elif rectangulo == "5":
                base = float(input("Ingresa  la base del rectangulo (numero entero): "))
                altura = float(input("Ingresa  la altura del rectangulo (numero entero): "))
                diagonal = (base ** 2 + altura ** 0.5)
                print("La diagonal del rectangulo es: ",diagonal)

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
            base = float(input("Ingresa el base del triangulo (numero entero): "))
            altura = float(input("Ingresa la altura del triangulo (numero entero): "))
            area = (base * altura) / 2
            print("El area del triangulo es : ",area)

        elif triangulo == "2":
            area = float(input("Ingresa el area del triangulo (numero entero): "))
            altura = float(input("Ingresa la altura del triangulo (numero entero): "))
            base = (2 * area) / altura
            print("La base del triangulo es : ",base)

        elif triangulo == 3:
            area = float(input("Ingresa el area del triangulo (numero entero): "))
            base = float(input("Ingresa el base del triangulo (numero entero): "))
            altura = (2 * area) / base
            print("La altura del triangulo es : ",altura)

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
            lado = float(input("Ingresa el lado del pentagono (numero entero): "))
            perimetro = 5 * lado
            print("El perimetro del pentagono es: ", perimetro)

        elif pentagono == "2":
            perimetro = float(input("Ingresa el perimetro del pentagono (numero entero): "))
            apotema = float(input("Ingresa la apotema del pentagono (numero entero): "))
            area = (perimetro * apotema) / 2
            print("El area del pentagono es: ", area)

        elif pentagono == "3":
            area = float(input("Ingresa el area del pentagono (numero entero): "))
            perimetro = float(input("Ingresa el perimetro del pentagono (numero entero): "))
            apotema = (2 * area) / perimetro
            print("La apotema del pentagono es: ", apotema)

    elif option == "5":
        print("""\nCase 5: Prisma rectangular\n
                    1. Calcular volumen
                    2. Calcular largo
                    3. Calcular ancho
                    4. Calcular altura\n""")

        prisma = (input("\nQue deseas calcular?: "))

        while prisma != "1" and prisma != "2" and prisma != "3" and prisma != "4":
            print("\nInvalid Option, Try again!")
            print("""\nCase 5: Prisma rectangular\n
                        1. Calcular volumen
                        2. Calcular largo
                        3. Calcular ancho
                        4. Calcular altura\n""")
            
            prisma = (input("\nQue deseas calcular?: "))

            while prisma != "1" and prisma != "2" and prisma != "3" and prisma != "4":
                print("\nInvalid Option, Try again!")
                print("""\nCase 5: Prisma rectangular\n
                            1. Calcular volumen
                            2. Calcular largo
                            3. Calcular ancho
                            4. Calcular altura\n""")

            prisma = (input("\nQue deseas calcular?: "))

        if prisma == "1":
            largo = float(input("Ingresa el largo del prisma (numero entero): "))
            ancho = float(input("Ingresa el ancho del prisma (numero entero): "))
            altura = float(input("Ingresa la altura del prisma (numero entero): "))
            volumen = largo * ancho * altura
            print("El volumen del prisma es: ", volumen)

        elif prisma == "2":
            volumen = float(input("Ingresa el volumen del prisma (numero entero): "))
            ancho = float(input("Ingresa el ancho del prisma (numero entero): "))
            altura = float(input("Ingresa la altura del prisma (numero entero): "))
            largo = volumen / (ancho * altura)
            print("El largo del prisma es: ", largo)

        elif prisma == "3":
            volumen = float(input("Ingresa el volumen del prisma (numero entero): "))
            largo = float(input("Ingresa el largo del prisma (numero entero): "))
            altura = float(input("Ingresa la altura del prisma (numero entero): "))
            ancho = volumen / (largo * altura)
            print("El ancho del prisma es: ", ancho)

        elif prisma == "4":
            volumen = float(input("Ingresa el volumen del prisma (numero entero): "))
            largo = float(input("Ingresa el largo del prisma (numero entero): "))
            ancho = float(input("Ingresa el ancho del prisma (numero entero): "))
            altura = volumen / (largo * ancho)
            print("La altura del prisma es: ", altura)

    elif option == "6":
        print("""\nCase 6: Esfera\n
                    1. Calcular volumen
                    2. Calcular radio\n""")

        esfera = (input("Que deseas calcular?: "))

        while esfera != "1" and esfera != "2":
            print("\nInvalid Option, Try again!")
            print("""\nCase 6: Esfera\n
                        1. Calcular volumen
                        2. Calcular radio\n""")
            
            esfera = (input("Que deseas calcular?: "))

        if esfera == "1":
            radio = float(input("Ingresa el radio de la esfera (numero entero): "))
            volumen = (4/3) * pi * (radio ** 3)
            print("El volumen de la esfera es: ", volumen)

        elif esfera == "2":
            volumen = float(input("Ingresa el volumen de la esfera (numero entero): "))
            radio = (volumen / ((4/3) * pi)) ** (1/3)
            print("El radio de la esfera es: ", radio)

    elif option == "7":
        print("""\nCase 7: Cilindro\n
                    1. Calcular volumen
                    2. Calcular radio
                    3. Calcular altura\n""")

        cilindro = (input("Que deseas calcular?: "))

        while cilindro != "1" and cilindro != "2" and cilindro != "3":
            print("\nInvalid Option, Try again!")
            print("""\nCase 7: Cilindro\n
                        1. Calcular volumen
                        2. Calcular radio
                        3. Calcular altura\n""")
            
            cilindro = (input("Que deseas calcular?: "))

        if cilindro == "1":
            radio = float(input("Ingresa el radio del cilindro (numero entero): "))
            altura = float(input("Ingresa la altura del cilindro (numero entero): "))
            volumen = pi * (radio ** 2) * altura
            print("El volumen del cilindro es: ", volumen)

        elif cilindro == "2":
            volumen = float(input("Ingresa el volumen del cilindro (numero entero): "))
            altura = float(input("Ingresa la altura del cilindro (numero entero): "))
            radio = (volumen / (pi * altura)) ** 0.5
            print("El radio del cilindro es: ", radio)

        elif cilindro == "3":
            volumen = float(input("Ingresa el volumen del cilindro (numero entero): "))
            radio = float(input("Ingresa el radio del cilindro (numero entero): "))
            altura = volumen / (pi * (radio ** 2))
            print("La altura del cilindro es: ", altura)

    elif option == "8":
        print("""\nCase 8: Cono\n
                    1. Calcular volumen
                    2. Calcular radio
                    3. Calcular altura\n""")

        cono = (input("Que deseas calcular?: "))

        while cono != "1" and cono != "2" and cono != "3":
            print("\nInvalid Option, Try again!")
            print("""\nCase 8: Cono\n
                        1. Calcular volumen
                        2. Calcular radio
                        3. Calcular altura\n""")

            cono = (input("Que deseas calcular?: "))

        if cono == "1":
            radio = float(input("Ingresa el radio del cono (numero entero): "))
            altura = float(input("Ingresa la altura del cono (numero entero): "))
            volumen = (1/3) * pi * (radio ** 2) * altura
            print("El volumen del cono es: ", volumen)

        elif cono == "2":
            volumen = float(input("Ingresa el volumen del cono (numero entero): "))
            altura = float(input("Ingresa la altura del cono (numero entero): "))
            radio = ((3 * volumen) / (pi * altura)) ** 0.5
            print("El radio del cono es: ", radio)

        elif cono == "3":
            volumen = float(input("Ingresa el volumen del cono (numero entero): "))
            radio = float(input("Ingresa el radio del cono (numero entero): "))
            altura = (3 * volumen) / (pi * (radio ** 2))
            print("La altura del cono es: ", altura)

    elif option == "9":
        print("""\nCase 9: Triangulo rectangulo\n
                    1. Calcular hipotenusa
                    2. Calcular cateto 1
                    3. Calcular cateto 2\n""")

        triangulo_r = (input("Que deseas calcular?: "))

        while triangulo_r != "1" and triangulo_r != "2" and triangulo_r != "3":
            print("\nInvalid Option, Try again!")
            print("""\nCase 9: Triangulo rectangulo\n
                        1. Calcular hipotenusa
                        2. Calcular cateto 1
                        3. Calcular cateto 2\n""")

        if triangulo_r == "1":
            cateto1 = float(input("Ingresa el cateto 1 (numero entero): "))
            cateto2 = float(input("Ingresa el cateto 2 (numero entero): "))
            hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** 0.5
            print("La hipotenusa es: ", hipotenusa)

        elif triangulo_r == "2":
            hipotenusa = float(input("Ingresa la hipotenusa (numero entero): "))
            cateto2 = float(input("Ingresa el cateto 2 (numero entero): "))
            cateto1 = (hipotenusa ** 2 - cateto2 ** 2) ** 0.5
            print("El cateto 1 es: ", cateto1)

        elif triangulo_r == "3":
            hipotenusa = float(input("Ingresa la hipotenusa (numero entero): "))
            cateto1 = float(input("Ingresa el cateto 1 (numero entero): "))
            cateto2 = (hipotenusa ** 2 - cateto1 ** 2) ** 0.5
            print("El cateto 2 es: ", cateto2)