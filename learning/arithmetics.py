num1 = int(input("Вкажіть перше число: "))
num2 = int(input("Вкажіть друге число: "))
operation = input("Вкажіть дію (+, -, *, /): ")


def arithmetic():
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        try:
            num1 // num2
        except ZeroDivisionError:
            print("На нуль ділити не можна!")
    else:
        print("Помилка: невідома операція!")


if __name__ == "__main__":
    arithmetic()
