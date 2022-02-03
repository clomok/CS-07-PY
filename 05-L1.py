first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
operator = input("Enter of one of the following operators: + | - | * | / |")

def add(num1, num2):
    descript = f"{num1}+{num2}"
    return f"The result of {descript} = {num1 + num2}"

def sub(num1, num2):
    descript = f"{num1}-{num2}"
    return f"The result of {descript} = {num1 - num2}"

def mult(num1, num2):
    descript = f"{num1}*{num2}"
    return f"The result of {descript} = {num1 * num2}"

def div(num1, num2):
    descript = f"{num1}/{num2}"
    return f"The result of {descript} = {num1 / num2}"

def calc():
    allowed_calculations = {"+": add, "-": sub, "*": mult, "/":div}
    try:
        result = allowed_calculations[operator](first_num, second_num)
        print(result)

    except KeyError:
        print("That operator doesn't exist.")
    except ZeroDivisionError:
        print("Can't divide by 0")

calc()
