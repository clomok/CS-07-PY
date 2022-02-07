try:
    num1 = int(input("Please enter a numerator: "))
    num2 = int(input("Enter the denominator: "))
    div = int(num1/num2)
    div_mod = (num1 % num2)
    print("Modulo type: ")
    print(type(div_mod))
    print(f"The modulo is {div_mod}")
    print()
    print("answer type: ")
    print(type(div))
    print(f"The answer is {div}.{div_mod}")

except ZeroDivisionError:
    print("Can't divide by Zero!")
except ValueError:
    print("Something went wrong!")
finally:
    print("This print sentence will run regardless")
raise Exception("Error because I said so!!")