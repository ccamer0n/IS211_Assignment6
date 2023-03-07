#5 test cases per test
#print a message for every test case

import unittest
import conversions

class KnownValues(unittest.TestCase):
    '''conversionTable = [Celsius, Fahrenheit, Kelvin]'''
    conversionTable = [[-273.15, -459.67, 0.0],
                       [-17.78, 0.0, 255.37],
                       [0.0, 32.0, 273.15],
                       [100, 212.0, 373.15],
                       [500, 932.0, 773.15]
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

if __name__ == '__main__':
    unittest.main()
