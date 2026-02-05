num = input("Nhap mot so nguyen: ")
total = 0
for digit in num:
    if digit.isdigit():
        total += int(digit)
print(f"Tong cua cac chu so {num} là: {total}")