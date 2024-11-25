num1 = int(input("Ingresa un numero aleatorio: "))
num2 = int(input("Ingresa nuevamente un numero aleatorio: "))
num3 = int(input("Ingresa nuevamente un numero aleatorio: "))
numeros = [num1, num2, num3]
numeros.sort()
print(f"El numero menores: {numeros[0]}")
print(f"El numero de en medio es: {numeros[1]}")
print(f"El numero mayor es: {numeros[2]}")
