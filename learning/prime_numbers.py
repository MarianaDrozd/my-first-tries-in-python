A = []
n = int(input("Input your number: "))
for x in range(2, n + 1):
    for y in range(2, x):
        if y == 1:
            break
        if x % y == 0:
            break
    else:
        A.append(x)
print(A)
