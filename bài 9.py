num = input("Nhập một số nguyen dương có 5 chữ số: ")
if len(num) == 5 and num.isdigit():
    max_digit = max(num)
    print(f"Chữ số lon nhất trong {num} là: {max_digit}")
else:
    print("Vui lòng nhập đung số có 5 chữ số.")