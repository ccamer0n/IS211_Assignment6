import unittest
import conversions
import conversions_refactored

class KnownValues(unittest.TestCase):
    '''conversionTable = [Celsius, Fahrenheit, Kelvin]'''
    conversionTable = [[-273.15, -459.67, 0.0],
                       [-17.78, 0.0, 255.37],
                       [0.0, 32.0, 273.15],
                       [100, 212.0, 373.15],
                       [500, 932.0, 773.15]
                       ]
    '''distanceConversion = [Miles, Yards, Meters]'''
    distanceConversion = [[0.05, 88, 80.47],
                          [0.25, 440, 402.34],
                          [0.5, 880.0, 804.67],
                          [1.0, 1760.0, 1609.34],
                          [10.0, 17600.0, 16093.44]
                          ]

    def test_convertCelsiusToKelvin(self):
        '''convertCelsiusToKelvin should give known result with known input'''
        for celsius, fahrenheit, kelvin in self.conversionTable:
            result = conversions.convertCelsiusToKelvin(celsius)
            self.assertEqual(kelvin, result)

    def test_convertCelsiusToFahrenheit(self):
        '''convertCelsiusToFahrenheit should give known result with known input'''
        for celsius, fahrenheit, kelvin in self.conversionTable:
            result = conversions.convertCelsiusToFahrenheit(celsius)
            self.assertEqual(fahrenheit, result)

    def test_convertFahrenheitToCelsius(self):
        '''convertFahrenheitToCelsius should give known result with known input'''
        for celsius, fahrenheit, kelvin in self.conversionTable:
            result = conversions.convertFahrenheitToCelsius(fahrenheit)
            self.assertEqual(celsius, result)

    def test_convertFahrenheitToKelvin(self):
        '''convertFahrenheitToKelvin should give known result with known input'''
        for celsius, fahrenheit, kelvin in self.conversionTable:
            result = conversions.convertFahrenheitToKelvin(fahrenheit)
            self.assertEqual(kelvin, result)

    def test_convertKelvinToCelsius(self):
        '''convertFahrenheitToKelvin should give known result with known input'''
        for celsius, fahrenheit, kelvin in self.conversionTable:
            result = conversions.convertKelvinToCelsius(kelvin)
            self.assertEqual(celsius, result)

    def test_convertKelvinToFahrenheit(self):
        '''convertFahrenheitToKelvin should give known result with known input'''
        for celsius, fahrenheit, kelvin in self.conversionTable:
            result = conversions.convertKelvinToFahrenheit(kelvin)
            self.assertEqual(fahrenheit, result)

#Testing the refactored conversion program:
    def test_refactoredCelsiusToKelvin(self):
        '''the convert function should give known result with known input'''
        for celsius, fahrenheit, kelvin in self.conversionTable:
            result = conversions_refactored.convert("Celsius", "Kelvin", celsius)
            self.assertEqual(kelvin, result)
    def test_refactoredCelsiusToFahrenheit(self):
        '''the convert function should give known result with known input'''
        for celsius, fahrenheit, kelvin in self.conversionTable:
            result = conversions_refactored.convert("Celsius", "Fahrenheit", celsius)
            self.assertEqual(fahrenheit, result)
    def test_refactoredFahrenheitToCelsius(self):
        '''the convert function should give known result with known input'''
        for celsius, fahrenheit, kelvin in self.conversionTable:
            result = conversions_refactored.convert("Fahrenheit", "Celsius", fahrenheit)
            self.assertEqual(celsius, result)
    def test_refactoredFahrenheitToKelvin(self):
        '''the convert function should give known result with known input'''
        for celsius, fahrenheit, kelvin in self.conversionTable:
            result = conversions_refactored.convert("Fahrenheit", "Kelvin", fahrenheit)
            self.assertEqual(kelvin, result)
    def test_refactoredKelvinToCelsius(self):
        '''the convert function should give known result with known input'''
        for celsius, fahrenheit, kelvin in self.conversionTable:
            result = conversions_refactored.convert("Kelvin", "Celsius", kelvin)
            self.assertEqual(celsius, result)
    def test_refactoredKelvinToFahrenheit(self):
        '''the convert function should give known result with known input'''
        for celsius, fahrenheit, kelvin in self.conversionTable:
            result = conversions_refactored.convert("Kelvin", "Fahrenheit", kelvin)
            self.assertEqual(fahrenheit, result)
    def test_refactoredMilesToYards(self):
        '''the convert function should give known result with known input'''
        for miles, yards, meters in self.distanceConversion:
            result = conversions_refactored.convert("Miles", "Yards", miles)
            self.assertEqual(yards, result)
    def test_refactoredMilesToMeters(self):
        '''the convert function should give known result with known input'''
        for miles, yards, meters in self.distanceConversion:
            result = conversions_refactored.convert("Miles", "Meters", miles)
            self.assertEqual(meters, result)
    def test_refactoredYardsToMiles(self):
        '''the convert function should give known result with known input'''
        for miles, yards, meters in self.distanceConversion:
            result = conversions_refactored.convert("Yards", "Miles", yards)
            self.assertEqual(miles, result)
    def test_refactoredYardsToMeters(self):
        '''the convert function should give known result with known input'''
        for miles, yards, meters in self.distanceConversion:
            result = conversions_refactored.convert("Yards", "Meters", yards)
            self.assertEqual(meters, result)
    def test_refactoredMetersToMiles(self):
        '''the convert function should give known result with known input'''
        for miles, yards, meters in self.distanceConversion:
            result = conversions_refactored.convert("Meters", "Miles", meters)
            self.assertEqual(miles, result)
    def test_refactoredMetersToYards(self):
        '''the convert function should give known result with known input'''
        for miles, yards, meters in self.distanceConversion:
            result = conversions_refactored.convert("Meters", "Yards", meters)
            self.assertEqual(yards, result)

#Test converting a unit to itself:
    def test_sameInputCelsius(self):
        '''the convert function should give the same value if converting a unit to itself'''
        for celsius, fahrenheit, kelvin in self.conversionTable:
            result = conversions_refactored.convert("Celsius", "Celsius", celsius)
            self.assertEqual(celsius, result)
    def test_sameInputKelvin(self):
        '''the convert function should give the same value if converting a unit to itself'''
        for celsius, fahrenheit, kelvin in self.conversionTable:
            result = conversions_refactored.convert("Kelvin", "Kelvin", kelvin)
            self.assertEqual(kelvin, result)
    def test_sameInputFahrenheit(self):
        '''the convert function should give the same value if converting a unit to itself'''
        for celsius, fahrenheit, kelvin in self.conversionTable:
            result = conversions_refactored.convert("Fahrenheit", "Fahrenheit", fahrenheit)
            self.assertEqual(fahrenheit, result)
    def test_sameInputMiles(self):
        '''the convert function should give the same value if converting a unit to itself'''
        for miles, yards, meters in self.distanceConversion:
            result = conversions_refactored.convert("Miles", "Miles", miles)
            self.assertEqual(miles, result)
    def test_sameInputYards(self):
        '''the convert function should give the same value if converting a unit to itself'''
        for miles, yards, meters in self.distanceConversion:
            result = conversions_refactored.convert("Yards", "Yards", yards)
            self.assertEqual(yards, result)
    def test_sameInputMeters(self):
        '''the convert function should give the same value if converting a unit to itself'''
        for miles, yards, meters in self.distanceConversion:
            result = conversions_refactored.convert("Meters", "Meters", meters)
            self.assertEqual(meters, result)

class BadInput(unittest.TestCase):
    badInput = ['A', '', '%', None]
    def test_celsiusToKelvinBadInput(self):
        '''convertCelsiusToKelvin should fail with non-numeric input'''
        for value in self.badInput:
            self.assertRaises(conversions.InvalidInputError, conversions.convertCelsiusToKelvin, value)

    def test_celsiusToFahrenheitBadInput(self):
        '''convertCelsiusToFahrenheit should fail with non-numeric input'''
        for value in self.badInput:
            self.assertRaises(conversions.InvalidInputError, conversions.convertCelsiusToFahrenheit, value)

    def test_fahrenheitToCelsiusBadInput(self):
        '''convertFahrenheitToCelsius should fail with non-numeric input'''
        for value in self.badInput:
            self.assertRaises(conversions.InvalidInputError, conversions.convertFahrenheitToCelsius, value)

    def test_fahrenheitToKelvinBadInput(self):
        '''convertFahrenheitToKelvin should fail with non-numeric input'''
        for value in self.badInput:
            self.assertRaises(conversions.InvalidInputError, conversions.convertFahrenheitToKelvin, value)

    def test_kelvinToCelsiusBadInput(self):
        '''convertKelvinToCelsius should fail with non-numeric input'''
        for value in self.badInput:
            self.assertRaises(conversions.InvalidInputError, conversions.convertKelvinToCelsius, value)

    def test_kelvinToFahrenheitBadInput(self):
        '''convertKelvinToFahrenheit should fail with non-numeric input'''
        for value in self.badInput:
            self.assertRaises(conversions.InvalidInputError, conversions.convertKelvinToFahrenheit, value)

#Check that converting incompatible units will raise a ConversionNotPossible exception:
    def test_incompatibleUnits(self):
        '''convert should fail if converting incompatible units'''
        self.assertRaises(conversions_refactored.ConversionNotPossible, conversions_refactored.convert, "Celsius", "Miles", 10)

if __name__ == '__main__':
    unittest.main()
