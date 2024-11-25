i = 'S'
totalpt = 0
totalh = 0
totalpz = 0
while i == 'S':
    print("Bienvenido a Pizzeria Raffaello")
    print("MENU")
    print("1: Pastas"),
    print("2: Hamburguesas"),
    print("3: Pizzas"),
    print("4: Salida")
    while True:
        m = int(input("Selecciona una opcion: "))
        if (m < 5):
            break
        else:
            print("Entrada no válida. Por favor, ingrese una opcion valida.")
    match m:
        case 1:
            p = 0
            while p < 3:
                print("Elige tu pasta")
                print("1: Pasta Alfredo $150")
                print("2: Pasta a la bolognesa $180")
                print("3: Volver al menu Principal")
                p = int(input("Seleciona tu Pasta: "))
                match p:
                    case 1:
                        price = 150
                        namep = "Pastas Alfredo"
                        cant = int(
                            input(f"¿Cuantas {namep} desea?: "))
                        subp = cant * price
                        totalpt = totalpt + subp
                    case 2:
                        price = 180
                        namep = "Pastas a la Bolognesa"
                        cant = int(
                            input(f"¿Cuantas {namep} desea?: "))
                        subp = cant * price
                        totalpt = totalpt + subp
        case 2:
            h = 0
            while h < 3:
                print("Elige tu hamburguesa")
                print("1: Hamburguesa premium $130")
                print("2: Hamburguesa de pollo $100")
                print("3: Volver al menu Principal")
                h = int(input("Seleciona tu Hamburguesa: "))
                match h:
                    case 1:
                        price = 130
                        nameh = "Hamburguesas Premium"
                        cant = int(
                            input(f"¿Cuantas {nameh} desea?: "))
                        subh = cant * price
                        totalh = totalh + subh
                    case 2:
                        price = 100
                        nameh = "Hamburguesas de Pollo"
                        cant = int(
                            input(f"¿Cuantas {nameh} desea?: "))
                        subh = cant * price
                        totalh = totalh + subh
        case 3:
            pz = 0
            while pz < 4:
                print("Elige tu pizza")
                print("1: Pizza mexicana $150")
                print("2: Pizza pepperoni $99")
                print("3: Pizza hawaina $120")
                print("4: Volver al menu")
                pz = int(input("Selecciona tu Pizza: "))
                match pz:
                    case 1:
                        price = 150
                        namepz = "Pizzas Mexicanas"
                        cant = int(
                            input(f"¿Cuantas {namepz} desea?: "))
                        subpz = price * cant
                        totalpz = totalpz + subpz
                    case 2:
                        price = 99
                        namepz = "Pizzas de Pepperoni"
                        cant = int(
                            input(f"¿Cuantas {namepz} desea?: "))
                        subpz = price * cant
                        totalpz = totalpz + subpz
                    case 3:
                        price = 120
                        namepz = "Pizzas Hawaianas"
                        cant = int(
                            input(f"¿Cuantas {namepz} desea?: "))
                        subpz = price * cant
                        totalpz = totalpz + subpz
    while True:
        i = str(input("¿Desea leer de nuevo el menu? (S/N): ")).upper()
        if i in ['S', 'N']:
            break
        else:
            print("Entrada no válida. Por favor, ingrese 'S' o 'N'.")
subt = totalpt + totalh + totalpz
iva = subt * 0.16
total = subt + iva
print(f"El total de las Pastas es de: ${totalpt}")
print(f"El total de las Hamburguesas es de: ${totalh}")
print(f"El total de las Pizzas es de: ${totalpz}")
print(f"El Subtotal de su compra es de: ${subt}")
print(f"El IVA de su compra es de: ${iva}")
print(f"El Total de su compra es de: ${total}")
