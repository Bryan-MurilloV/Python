month = int(input("Ingrese un mes del año con numero: "))
options = {
    1: "Este mes tiene 31 dias",
    2: "Este mes tiene 28 dias",
    3: "Este mes tiene 31 dias",
    4: "Este mes tiene 30 dias",
    5: "Este mes tiene 31 dias",
    6: "Este mes tiene 30 dias",
    7: "Este mes tiene 31 dias",
    8: "Este mes tiene 31 dias",
    9: "Este mes tiene 30 dias",
    10: "Este mes tiene 31 dias",
    11: "Este mes tiene 30 dias",
    12: "Este mes tiene 31 dias"
}
print(options.get(month))
