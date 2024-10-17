# Temperature conversion
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

temp=float(input("Enter your temperature: "))

if unit == "C":
    temp  = round((temp*9)/5+32,1)
    print(f"The temperature in Fahrenheit is: {temp}")
elif unit == "F":
    temp  = round((temp-32)*5/9,1)
    print(f"The temperature in Celsius is: {temp}")
else: 
    print(f"{unit} is invalid")

