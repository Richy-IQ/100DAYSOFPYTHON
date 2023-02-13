#!/usr/bin/python3

#calculator
#add
def add(n1, n2):
  return n1 + n2
#subtract
def subtract(n1, n2):
  return n1 - n2
#multiply 
def multiply(n1, n2):
  return n1 * n2
#divide
def divide(n1, n2):
  return n1 / n2
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
num1 = int(input("what is your first number: "))
for operation in operations:
  print(operation)
operation_symbol = input("pick an operation from the line above ")
num2 = int(input("what is your second number: "))
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")
