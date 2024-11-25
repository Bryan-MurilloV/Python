print("\nBienvenido a tu Sistema de Ahorro \n")
nom = input("¿Como te llamas? \n").title()
edad = int(input(f"Por favor {nom} ingresa tu edad.\n"))
if edad >= 18:
    print(f"Hola {nom}, ¿Cual es tu objetivo? ")
    objetivo = str(input()).title().strip()
    precio_objetivo = int(input(f"{nom}, ¿Cuanto cuesta tu {objetivo}? \n$"))
    tiempo = int(input(f"{nom}, ¿En cuantos meses quieres tu {objetivo}?\n"))
    ingreso = int(input(f"{nom}, ¿Cual es tu salario mensual?\n$"))
    print(f"Muy bien {nom}, ahora vamos a ver tus gastos.")
    # variables inicializadas
    gastos = 0
    costo_medicamento = 0
    renta = 0
    luz = 0
    tel = 0
    consultas = 0
    total_hormiga = 0
    total_antojos = 0
    total_ginnecesarios = 0
    total_aliment = 0
    total_servicios = 0
    total_entretenimiento = 0
    total_innecesarios = 0
    # variables inicializadas
    while gastos < 6:
        print(
            " 1: Servicios\n 2: Alimentacion\n 3: Salud\n 4: Entretenimiento\n 5: Innecesarios\n 6: Terminar"
        )
        gastos = int(input("¿Que gastos desea registrar?\n"))
        match gastos:
            case 1:
                print("Primero, veamos los gastos en servicios al mes")
                s = "No"
                while s == "No":
                    print(" 1: Rentas\n 2: Luz \n 3: Telefono")
                    servicio = int(input(
                        "Seleccione el servicio que desea registrar\n"))
                    match servicio:
                        case 1:
                            renta = int(
                                input("¿Cuanto pagas de renta mensualmente?\n$"))
                        case 2:
                            luz = int(
                                input("¿Cuanto pagas de luz mensualmente\n$"))
                        case 3:
                            tel = int(
                                input("¿Cuanto pagas por el telefono mensualmente?\n$"))
                    while True:
                        s = str(input("¿Ha terminado de ingresar los gastos de sus servicios? (Si/No): ")
                                ).capitalize().strip()
                        if s in ["Si", "No"]:
                            break
                        else:
                            print("¿Si o No?")
            case 2:
                print("Veamos lo que gastas en tu alimentacion.")
                total_aliment = 0
                i = 0
                while i < 4:
                    print(
                        " 1: Pollo\n 2: Carne de res \n 3: Comida en la calle\n 4: Mandado")
                    i = int(input(
                        "Seleccione el servicio que desea registrar\n"))
                    match i:
                        case 1:
                            nombre_gasto = "Pollo"
                            precio = 200
                            print(f"{nombre_gasto}---${precio}")
                            cantidad = int(input(
                                f"¿Cuanto de {nombre_gasto} comes al mes?\n"))
                            subtotal_aliment = (cantidad * precio)
                            total_aliment = total_aliment + subtotal_aliment
                        case 2:
                            nombre_gasto = "Carne de res"
                            precio = 180
                            print(f"{nombre_gasto}---${precio}")
                            cantidad = int(input(
                                f"¿Cuanto de {nombre_gasto} comes al mes?\n"))
                            subtotal_aliment = (cantidad * precio)
                            total_aliment = total_aliment + subtotal_aliment
                        case 3:
                            nombre_gasto = "Comida en la calle"
                            precio = 150
                            print(f"{nombre_gasto}---${precio}")
                            cantidad = int(input(
                                f"¿Cuanta {nombre_gasto} comes al mes?\n"))
                            subtotal_aliment = (cantidad * precio)
                            total_aliment = total_aliment + subtotal_aliment
                        case 4:
                            m = "No"
                            while m == "No":
                                print("Mandado")
                                print(" 1: Cereal\n 2: Cafe\n 3: Leche")
                                mandado = int(input(
                                    "Ingrese el procuto de mandado que desea registrar.\n"))
                                match mandado:
                                    case 1:
                                        nombre_gasto = "Cereal"
                                        precio = 57
                                        print(f"{nombre_gasto}---${precio}")
                                        cantidad = int(input(
                                            f"¿Cuanto {nombre_gasto} compras al mes?\n"))
                                        subtotal_aliment = (cantidad * precio)
                                        total_aliment = total_aliment + subtotal_aliment
                                    case 2:
                                        nombre_gasto = "Cafe"
                                        precio = 127
                                        print(f"{nombre_gasto}---${precio}")
                                        cantidad = int(input(
                                            f"¿Cuanto {nombre_gasto} compras al mes?\n"))
                                        subtotal_aliment = (cantidad * precio)
                                        total_aliment = total_aliment + subtotal_aliment
                                    case 3:
                                        nombre_gasto = "Leche"
                                        precio = 40
                                        print(f"{nombre_gasto}---${precio}")
                                        cantidad = int(input(
                                            f"¿Cuanto {nombre_gasto} compras al mes?\n"))
                                        subtotal_aliment = (cantidad * precio)
                                        total_aliment = total_aliment + subtotal_aliment
                                while True:
                                    m = str(input("¿Ha terminado de ingresar los gastos de mandado? (Si/No): ")
                                            ).capitalize().strip()
                                    if m in ["Si", "No"]:
                                        break
                                    else:
                                        print("¿Si o No?")
            case 3:
                print("Gastos medicos")
                g = "No"
                while g == "No":
                    print(" 1: Medicamentos\n 2: Consultas")
                    servicio = int(input(
                        "Seleccione el servicio que desea registrar\n"))
                    match servicio:
                        case 1:
                            costo_medicamento = int(
                                input("¿Cuanto te cuesta el medicamento por mes?\n$"))
                        case 2:
                            precio = int(
                                input("¿Cuanto cuesta tu consulta medica?\n$"))
                            cantidad = int(input("¿Cuantas por mes?\n"))
                            consultas = precio * cantidad
                    while True:
                        g = str(input("¿Ha terminado de ingresar los gastos medicos? (Si/No): ")
                                ).capitalize().strip()
                        if g in ["Si", "No"]:
                            break
                        else:
                            print("¿Si o No?")
            case 4:
                print("¿Cuanto gastas cuando sales a divertirte?")
                total_entretenimiento = 0
                e = "No"
                while e == "No":
                    print(" 1: Cine\n 2: Salidas \n 3: Amigos")
                    servicio = int(input(
                        "Seleccione el servicio que desea registrar\n"))
                    match servicio:
                        case 1:
                            precio = 180
                            print(f"Cine----${precio}")
                            cantidad = int(
                                input("¿Cuantas veces al mes vas al cine?\n"))
                            subtotal_entretenimiento = precio * cantidad
                            total_entretenimiento = total_entretenimiento + subtotal_entretenimiento
                        case 2:
                            precio = 200
                            print(f"Salidas----${precio}")
                            cantidad = int(
                                input("¿Cuantas veces al mes sales?\n"))
                            subtotal_entretenimiento = precio * cantidad
                            total_entretenimiento = total_entretenimiento + subtotal_entretenimiento
                        case 3:
                            precio = 100
                            print(f"Amigos----${precio}")
                            cantidad = int(
                                input("¿Cuantas veces al mes vas con amigos?\n"))
                            subtotal_entretenimiento = precio * cantidad
                            total_entretenimiento = total_entretenimiento + subtotal_entretenimiento
                    while True:
                        e = str(input("¿Ha terminado de ingresar los gastos relacionados a su diversion? (Si/No): ")
                                ).capitalize().strip()
                        if e in ["Si", "No"]:
                            break
                        else:
                            print("¿Si o No?")
            case 5:
                print("Finalmente conntabilizaremos tus gastos innecesarios.")
                n = "No"
                while n == "No":
                    print(" 1: Hormiga\n 2: Antojos \n 3: Innecessarios")
                    servicio = int(input(
                        "Seleccione el servicio que desea registrar\n"))
                    match servicio:
                        case 1:
                            hormiga = int(
                                input("¿Cuanto gastas en gastos hormiga a la semana?\n$"))
                            total_hormiga = hormiga * 4
                        case 2:
                            antojos = int(
                                input("¿Cuanto gastas en antojos a la semana?\n$"))
                            total_antojos = antojos * 4
                        case 3:
                            innecesarios = int(
                                input("¿Cuanto gasto innecesario haces a la semana?\n$"))
                            total_ginnecesarios = innecesarios * 4
                    while True:
                        n = str(input("¿Ha terminado de ingresar los gastos innecesarios? (Si/No): ")
                                ).capitalize().strip()
                        if n in ["Si", "No"]:
                            break
                        else:
                            print("¿Si o No?")
    total_servicios = renta + luz + tel
    total_salud = costo_medicamento + consultas
    total_innecesarios = total_hormiga + total_antojos + total_ginnecesarios
    gasto_mensual = total_aliment + total_servicios + \
        total_salud + total_entretenimiento + total_innecesarios
    print(f"El total de los servicios es: ${total_servicios}")
    print(f"El total de alimentacion es de: ${total_aliment}")
    print(f"El total en salud es de: ${total_salud}")
    print(f"El total de entretenimiento es de: ${total_entretenimiento}")
    print(f"El total de gastos innecesarios es de: ${total_innecesarios}")
    print(f"GASTO TOTAL MENSUAL-----${gasto_mensual}")
    restante = ingreso - gasto_mensual
    print(f"{nom}, Puedes ahorrar ${restante} al mes.")
    print(f"Pero puedes ahorrar otros ${
        total_innecesarios} si no gastas en innecesarios.")
    mas_ahorro = str(input("¿Quieres ahorrrarlos?\n")).capitalize().strip()
    if mas_ahorro == "Si":
        restante = restante + total_innecesarios
    else:
        restante = restante + 0
    print(f"Ok {nom}. Tu ahorro ahora es de ${restante}")

    def ahorro(restante, precio_objetivo, tiempo):
        meses = [
            "enero", "febrero", "marzo", "abril", "mayo", "junio",
            "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
        ]
        while True:
            mes_inicial = input("¿En que mes estamos?: ").strip().lower()
            if mes_inicial in meses:
                break
            print("Mes no válido. Por favor, intenta de nuevo.")
        incremento = restante
        mes_actual = meses.index(mes_inicial)
        ahorro_actual = restante
        meses_transcurridos = 0
        while ahorro_actual < precio_objetivo and meses_transcurridos < tiempo:
            print(f"{meses[mes_actual].capitalize()}: ${ahorro_actual}")
            ahorro_actual += incremento
            mes_actual = (mes_actual + 1) % 12
            meses_transcurridos += 1
        if ahorro_actual >= precio_objetivo:
            print(f"{meses[mes_actual].capitalize()}: ${
                ahorro_actual} ({nom}, El objetivo se alcanzo en {meses_transcurridos} meses)")
        else:
            ahorro_faltante = precio_objetivo - ahorro_actual
            print(f"{nom}, No se alcanzó el objetivo en {tiempo} meses.\n")
            print(f"Faltaron ${ahorro_faltante} para alcanzar el objetivo.\n")
            meses_adicionales = 0
            while ahorro_actual < precio_objetivo:
                print(f"{meses[mes_actual].capitalize()
                         } ${ahorro_actual}")
                ahorro_actual += incremento
                mes_actual = (mes_actual + 1) % 12
                meses_adicionales += 1
            print(f"{meses[mes_actual].capitalize()}: ${
                ahorro_actual} Objetivo alcanzado\n")
            print(f"Se necesitaron {
                meses_adicionales} meses adicionales para alcanzar el objetivo.\n")

    ahorro(restante, precio_objetivo, tiempo)
else:
    print(f"{nom} no puedes hacer un plan de ahorro porque eres menor de edad.")
