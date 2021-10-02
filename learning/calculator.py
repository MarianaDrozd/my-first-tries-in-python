from colorama import init
from colorama import Fore, Back

init()
print(Fore.BLACK)
print(Back.GREEN)
what = input("Що будемо робити? (+, -, *, /):")
print(Back.CYAN)
a = float(input("Вкажіть перше число: "))
b = float(input("Вкажіть друге число: "))
print(Back.YELLOW)
if what == "+":
    c = a + b
    print("Результат: " + str(c))
elif what == "-":
    c = a - b
    print("Результат: " + str(c))
elif what == "*":
    c = a * b
    print("Результат: " + str(c))
elif what == "/":
    c = a / b
    print("Результат: " + str(c))
else:
    print("Помилка! Спробуйте ще раз :)")

input()
