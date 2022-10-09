# Simple Celsius to fahrenheit converter

temp = int(input("Enter temp value: "))
unit = str(input("c or f?:  "))

if unit == "c":
  conversion = 9/5 * temp + 32
  print(" Your converted temp is:", conversion, "°F")
elif unit == "f":
  conversion = 5/9 * (temp - 32)
  print(" Your converted temp is:", conversion, "°C")
else:
  print("Enter a proper value!")