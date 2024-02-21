num1 = float(input("enter number\t"))
num2 = float(input("enter number\t"))
action = input("enter operator\t")
match action:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        print(num1 / num2)
