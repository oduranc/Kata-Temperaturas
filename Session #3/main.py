class Scales:

    #Scales
    Kelvin = "°K"
    Celsius = "°C"
    Fahrenheit = "°F"

class Temperature:

    # Attributes
    value = 0
    scale = ""

    # Constructor
    def __init__(self, value, scale):
        self.value = value
        self.scale = scale

    # Methods

    # Add Temperatures
    def Add(T1, T2):
        T1, T2 = Temperature.MatchScales(T1, T2)
        Result = T1.value + T2.value
        return f"{round(Result, 5)} {T1.scale}"

    # Substract Temperatures
    def Substract(T1, T2):
        T1, T2 = Temperature.MatchScales(T1, T2)
        Result = T1.value - T2.value
        return f"{round(Result, 5)} {T1.scale}"

    # Multiply Temperatures
    def MultiplyBy(T1, T2):
        T1, T2 = Temperature.MatchScales(T1, T2)
        Result = T1.value * T2.value
        return f"{round(Result, 5)} {T1.scale}"

    # Divide Temperatures
    def DivideBy(T1, T2):
        T1, T2 = Temperature.MatchScales(T1, T2)
        if T2.value != 0:
            Result = T1.value / T2.value
            return f"{round(Result, 5)} {T1.scale}"
        else:
            raise ValueError("Can't divide by zero!")

    # Compare Scales and match them
    def MatchScales(T1, T2):
        if T1.scale == Scales.Celsius:
            Temperature.ToCelsius(T2)
        elif T1.scale == Scales.Fahrenheit:
            Temperature.ToFahrenheit(T2)
        elif T1.scale == Scales.Kelvin:
            Temperature.ToKelvin(T2)
        else:
            raise ValueError("Not a scale.")
        return T1, T2

    # Convert To Fahrenheit
    def ToFahrenheit(T):
        if T.scale == Scales.Celsius:
            T.value = (T.value * 1.8) + 32
        elif T.scale == Scales.Kelvin:
            T.value = (9 / 5) * (T.value - 273.15) + 32
        elif T.scale != Scales.Fahrenheit:
            raise ValueError("Not a scale.")
        T.scale = Scales.Fahrenheit
        return T

    # Convert To Celsius
    def ToCelsius(T):
        if T.scale == Scales.Fahrenheit:
            T.value = (T.value - 32) / 1.8
        elif T.scale == Scales.Kelvin:
            T.value = T.value - 273.15
        elif T.scale != Scales.Celsius:
            raise ValueError("Not a scale.")
        T.scale = Scales.Celsius
        return T

    # Convert To Kelvin
    def ToKelvin(T):
        if T.scale == Scales.Celsius:
            T.value = T.value + 273.15
        elif T.scale == Scales.Fahrenheit:
            T.value = ((5 * (T.value - 32)) / 9) + 273.15
        elif T.scale != Scales.Kelvin:
            raise ValueError("Not a scale.")
        T.scale = Scales.Kelvin
        return T