print("Enter a number:")

number1 = int(input())

print("Enter a second number:")

number2 = int(input())

operator = input("Enter a number to 1)Multiply 2)Divide 3)Add 4)Subtract :   ")

operator = int(operator)

if operator == 1:
  result = number1 * number2
  print(result)
elif operator == 2:
  result = number1 / number2
  print(result)
elif operator == 3:
  result = number1 + number2
  print(result)
elif operator == 4:
  result = number1 - number2
  print(result)
else:
  print("Enter a correct number")