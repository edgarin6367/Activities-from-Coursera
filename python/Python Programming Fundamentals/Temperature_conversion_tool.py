# celsius_to_fahrenheit(celsius): Takes a temperature in Celsius and converts it to Fahrenheit.
def celsius_to_fahrenheit(celsius:int):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
# fahrenheit_to_celsius(fahrenheit): Takes a temperature in Fahrenheit and converts it to Celsius.
def fahrenheit_to_celsius(fahrenheit:int):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
# convert_temperature(temperature, unit): Takes a temperature value and a unit ('C' for Celsius or 'F' for Fahrenheit). It calls the appropriate conversion function based on the unit and returns the converted temperature.
def convert_temperature(temperature:int, unit:str):
    if unit == 'C':
        return celsius_to_fahrenheit(temperature_c)
    elif unit == 'F':
        return fahrenheit_to_celsius(temperature_f)
    else:
        print("No valid unit for temperature")
        
temperature_c = 25
temperature_f = 77

converted_f = convert_temperature(temperature_c, 'C')
converted_c = convert_temperature(temperature_f, 'F')

print(f"",temperature_c,"°C is equal to ", converted_f,"°F")
print(f"",temperature_f,"°F is equal to ", converted_c,"°C")
