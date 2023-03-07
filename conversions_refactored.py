#formulas = {"toUnit": ("fromUnit", "formula")}
value = 0
formulas = {("Fahrenheit", "Celsius"): (value * (9 / 5) + 32)}


def convert(fromUnit, toUnit, value):
    formula = formulas.get((toUnit, fromUnit))

    return formula





