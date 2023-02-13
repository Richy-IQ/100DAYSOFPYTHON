#!/usr/bin/python3
#calculator
#add
from art import logo
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

def calculator():
  print(logo)
  num1 = int(input("what is your first number: "))
  for operation in operations:
    print(operation)
  should_continue = True
  while should_continue:
    operation_symbol = input("pick an operation ")
    num2 = int(input("what is your next number: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    if input(f"type 'y' to continue calculating with {answer} or type 'n' to exit.: ") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()
calculator()      
