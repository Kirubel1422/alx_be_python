FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return 32 + celsius * CELSIUS_TO_FAHRENHEIT_FACTOR 

temp_value = float(input("Enter the temperature to convert: "))
temp_scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if temp_scale.lower() not in ["c", "f"]:
    raise ValueError("Invalid temperature. Please enter a numeric value.")

if temp_scale.lower() == "f":
    result = convert_to_celsius(temp_value)
else:
    result = convert_to_fahrenheit(temp_value)

print(f"{temp_value}°{temp_scale.upper()} is {result}°{list(set(['C', 'F']).difference([temp_scale.upper()]))[0]}")
