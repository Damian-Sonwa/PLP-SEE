# Ask the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


# Ask the user to select an opertion
operation = input("Choose an operation(+, -, *, /): ")

# Perform the action based on the operation
if operation == '+':
  print("Result:" , num1 + num2)
elif operation == '-':
  print("Result:" ,  num1 - num2)
elif operation == '*':
  
  print("Result:" , num1 * num2)
elif operation == '/':
    if num2  != 0:
     print("Result:", num1 / num2)
    else:
     print("Error: Cannot divide by zero.") 
 
else:
    print("Invalid operation") 


 