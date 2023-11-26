from art import logo

#calculator
# add 
def add(a, b):
    return a+b

# subtract
def subtract(a, b):
    return a-b
    
# multiply
def multiply(a, b):
    return a*b
    
# divide
def divide(a, b):
    return a/b

operations = {
    "+": add, 
    "-": subtract, 
    "*":multiply, 
    "/":divide
}
def calculator():
    print(logo)
    num1 = float(input("what's the first number?: "))
    
    for key in operations:
        print(key)
    continue_calc = True
    while continue_calc:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("what's the next number?: "))
        
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        is_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
        if is_continue == 'n':
            continue_calc = False
            calculator()
        elif is_continue == 'y':
            num1 = answer
        else:
            print("you have entered a wrong input. ")

calculator()
