class ConversionNotPossible(ValueError):
    pass
def convert(fromUnit, toUnit, value):
    '''Converts a unit of a specified type and value to another specified type'''
    formulas = {("Celsius", "Fahrenheit"): (value * (9 / 5) + 32),
                ("Kelvin", "Fahrenheit"): (value * (9 / 5) - 459.67),
                ("Fahrenheit", "Celsius"): ((value - 32) * (5 / 9)),
                ("Kelvin", "Celsius"): (value - 273.15),
                ("Fahrenheit", "Kelvin"): ((value + 459.67) * (5 / 9)),
                ("Celsius", "Kelvin"): (value + 273.15),
                ("Miles", "Yards"): (value * 1760),
                ("Miles", "Meters"): (value * 1609.344),
                ("Yards", "Miles"): (value / 1760),
                ("Yards", "Meters"): (value * 0.9144),
                ("Meters", "Miles"): (value / 1609.344),
                ("Meters", "Yards"): (value / 0.9144)
                }

    if fromUnit == toUnit:
        return value
    elif formulas.get((fromUnit.capitalize(), toUnit.capitalize())) == None:
        raise ConversionNotPossible(f"Cannot convert {fromUnit} to {toUnit}")
    else:
        result = round(formulas.get((fromUnit.capitalize(), toUnit.capitalize())), 2)
        return result

