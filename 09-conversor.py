temperatura = float(input("Ingrese temperatura:"))
escala = input("Es Farenheit(F) o Celcius(C):").lower()

if escala == "f":
    celsius = (temperatura - 32) * 5/9
    print("La temperatura en celsius es: ", celsius)
elif escala == "c":
    farenheit = temperatura * 1.8 + 32
    print("La temperatura en farenheit es: ", farenheit)
else:
    print("Escala incorrecta")
