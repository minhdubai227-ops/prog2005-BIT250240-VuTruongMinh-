num = int(input("Nhập một số nguyên dương: "))
original = num
total = 0
while num > 0:
    digit = num % 10
    total += digit
    num //= 10
print(f"Tổng các chữ số của {original} là: {total}")