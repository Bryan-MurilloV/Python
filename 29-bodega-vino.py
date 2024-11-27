lista_vino2 = []
lista_vino3 = []
subtotalvino = 0
totalvino = 0
i = 'Si'
año = 0
while i == 'Si':
    año += 1
    vino1 = int(input(f"Ingrese lo producido del vino 1 en el año {año}\n"))
    vino2 = int(input(f"Ingrese lo producido del vino 2 en el año {año}\n"))
    lista_vino2.append(vino2)
    vino3 = int(input(f"Ingrese lo producido del vino 3 en el año {año}\n"))
    lista_vino3.append(vino3)
    vino4 = int(input(f"Ingrese lo producido del vino 4 en el año {año}\n"))
    vino5 = int(input(f"Ingrese lo producido del vino 5 en el año {año}\n"))
    subtotalvino = vino1 + vino2 + vino3 + vino4 + vino5
    totalvino = totalvino + subtotalvino
    while True:
        i = input("¿Nuevo Año?\n").capitalize().strip()
        if i in ['Si', 'No']:
            break
        else:
            print("Solo \"Si\" o \"No\"")
vin = sorted(lista_vino2)
añovin2 = lista_vino2.index(vin[-1])+1
print(f"El año con mas Vino del tipo 2 fue el año {
      añovin2} con {vin[-1]} Lts.")
if 0 in lista_vino3:
    print(f"El año {lista_vino3.index(0)+1} no se produjo Vino del tipo 3.")
else:
    print("No hubo años con nula produccion del Vino tipo 3")
print(f"El total de Vino en {año} años fue de {totalvino} Lts.")
