saludo = 25


def saludar():
    global saludo
    saludo = "Hola Mundo"


def saludaChanchito():
    saludo = "Hola Chanchito"
    print(saludo)


resultado1 = saludo + 3
print(resultado1)
saludar()
resultado2 = saludo + 3
print(resultado2)
