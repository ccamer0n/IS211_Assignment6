class InvalidInputError(ValueError):
    pass

def convertCelsiusToKelvin(celsius):
    '''Takes in a float representing a Celsius measurement,
    and returns that temperature converted into Kelvins'''
    if not isinstance(celsius, float):
        if not isinstance(celsius, int):
            raise InvalidInputError("input must be a number.") 
    kelvin = round((celsius + 273.15), 2)
    return kelvin


def convertCelsiusToFahrenheit(celsius):
    '''Takes in a float representing a Celsius measurement,
    and returns that temperature converted into Fahrenheit'''
    if not isinstance(celsius, float):
        if not isinstance(celsius, int):
            raise InvalidInputError("input must be a number.")
    fahrenheit = round((celsius * (9 / 5) + 32), 2)
    return fahrenheit

def convertFahrenheitToCelsius(fahrenheit):
    '''Takes in a float representing a Fahrenheit measurement,
    and returns that temperature converted into Celsius'''
    if not isinstance(fahrenheit, float):
        if not isinstance(fahrenheit, int):
            raise InvalidInputError("input must be a number.")
    celsius = round(((fahrenheit - 32) * (5 / 9)), 2)
    return celsius

def convertFahrenheitToKelvin(fahrenheit):
    '''Takes in a float representing a Fahrenheit measurement,
    and returns that temperature converted into Kelvins'''
    if not isinstance(fahrenheit, float):
        if not isinstance(fahrenheit, int):
            raise InvalidInputError("input must be a number.")
    kelvin = round(((fahrenheit + 459.67) * (5 / 9)), 2)
    return kelvin

def convertKelvinToCelsius(kelvin):
    '''Takes in a float representing a Kelvin measurement,
    and returns that temperature converted into Celsius'''
    if not isinstance(kelvin, float):
        if not isinstance(kelvin, int):
            raise InvalidInputError("input must be a number.")
    celsius = round((kelvin - 273.15), 2)
    return celsius

def convertKelvinToFahrenheit(kelvin):
    '''Takes in a float representing a Kelvin measurement,
    and returns that temperature converted into Fahrenheit'''
    if not isinstance(kelvin, float):
        if not isinstance(kelvin, int):
            raise InvalidInputError("input must be a number.")
    fahrenheit = round((kelvin * (9 / 5) - 459.67), 2)
    return fahrenheit
