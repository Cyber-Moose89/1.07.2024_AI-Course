####
####
####
####
####
####

a = float(input("Enter First Number: "))
symbol = input("Enter Symbol (+, -, *, /): ")
b = float(input("Enter Second Number: "))

oper= {
    '+': a + b,
    '-': a - b,
    '*': a * b,
    '/': a / b if b != 0 else "Error! Division by zero."
}

result = oper.get(symbol, "Invalid symbol.")
print(f"The result is: {result}")
