n = int(input("Nhập một sô nguyên dương: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Giai thừa của {n} là: {factorial}")