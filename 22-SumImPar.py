par = 0
impar = 0
i = 1
rango = int(input("Introduzca hasta que numero desea sumar: "))
while i <= rango:
    if (i % 2) == 0:
        par = par + i
    else:
        impar = impar + i
    i = i + 1
print(f"La suma de los numeros pares desde 1 hasta {rango} es de: {par} ")
print(f"La suma de los numeros impares desde 1 hasta {rango} es de: {impar}")