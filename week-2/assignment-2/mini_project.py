print("Temperature Converter")
print("---------------------")

fahrenheit = float(input("What is the temperature in Fahrenheit where you live now? "))
celsius = (fahrenheit - 32) * 5 / 9

print(f"{fahrenheit:.1f}°F is {celsius:.1f}°C.")
