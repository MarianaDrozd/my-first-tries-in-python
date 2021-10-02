what = input("Що будемо робити? (+, -, *, /):")
a = float(input("Вкажіть перше число: "))
b = float(input("Вкажіть друге число: "))

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
