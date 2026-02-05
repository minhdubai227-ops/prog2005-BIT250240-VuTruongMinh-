n = int(input("Nhập n: "))
total_odd = 0
for i in range(1, n + 1, 2):
    total_odd += i
print(f"Tổng các số lẻ từ 1 đến {n} là: {total_odd}")