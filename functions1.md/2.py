def fahrenheit_to_centigrade(fahrenheit):
    centigrade = (5 / 9) * (fahrenheit - 32)
    return centigrade


fahrenheit = float(input("Enter temperature in Fahrenheit: "))
centigrade = fahrenheit_to_centigrade(fahrenheit)
print(f"Equivalent temperature in Centigrade: {centigrade}")
