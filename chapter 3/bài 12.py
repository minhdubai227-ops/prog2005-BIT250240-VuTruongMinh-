m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))
print("Nhập ma trận thứ nhất:")
ma_tran1 = []
for i in range(m):
    print(f"Nhập {n} số của hàng {i+1}, cách nhau bằng khoảng trắng:")
    hang = [float(x) for x in input().split()]
    ma_tran1.append(hang)
print("Nhập ma trận thứ hai:")
ma_tran2 = []
for i in range(m):
    print(f"Nhập {n} số của hàng {i+1}, cách nhau bằng khoảng trắng:")
    hang = [float(x) for x in input().split()]
    ma_tran2.append(hang)
ket_qua = []
for i in range(m):
    hang = []
    for j in range(n):
        hang.append(ma_tran1[i][j] + ma_tran2[i][j])
    ket_qua.append(hang)
print("Kết quả cộng hai ma trận:")
for hang in ket_qua:
    print(hang)