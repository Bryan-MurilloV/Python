def convertidor(decimal):
    listabin = []
    while (decimal >= 1):
        digitos = decimal % 2
        decimal = decimal // 2
        listabin.append(digitos)
    return listabin


decimal = int(input("Ingresa el numero a convertir a binario:\n"))
binario = convertidor(decimal)
print(f"El {decimal} en binario es: {binario[::-1]}\n")
