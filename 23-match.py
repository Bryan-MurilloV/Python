day = int(input("Ingresa un dia de la semana con numero: "))
match day: 
    case 1:
        print("Hoy es lunes y te levantas a las 6:00")
    case 2 :
        print("Hoy es martes y te levantas a las 6:00")
    case 3 :
        print("Hoy es miercoles y te levantas a las 6:00")
    case 4 :
        print("Hoy es jueves y te levantas a las 6:00")
    case 5 :
        print("Hoy es viernes y te levantas a las 6:00")
    case 6 :
        print("Hoy es sabado hoy descansas")
    case 7 :
        print("Hoy es domingo hoy descansas")
    case _:
        print("No es un dia de la semana")