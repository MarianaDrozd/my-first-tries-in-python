year = int(input("Input your year, please: "))
if year % 4 == 0 and year % 100 != 0:
    print("Your year is leap!")
elif year % 400 == 0:
    print("Your year is leap!")
else:
    print("Your year is usual!")
