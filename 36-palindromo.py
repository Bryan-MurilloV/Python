def no_espacio(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


def reves(texto):
    texto_reves = ""
    for char in texto:
        texto_reves = char + texto_reves
    return texto_reves


def es_palindromo(texto):
    texto = no_espacio(texto)
    texto_reves = reves(texto)
    return texto.lower() == texto_reves.lower()


texto = input("Ingrese su frase o palabra:\n")
if es_palindromo(texto) is True:
    print(f"{texto}, es Palindromo.")
else:
    print(f"{texto}, no es Palindromo.")
