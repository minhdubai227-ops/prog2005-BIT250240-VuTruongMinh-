import random
M = int(input("số hàng M: "))
N = int(input("số cột N: "))
ma_tran = [[random.randint(1, 100) for j in range(N)] for i in range(M)]
print("Ma trận:")
for hang in ma_tran:
    print(hang)
hang_so = int(input("số hàng cần xem: "))
if 0 <= hang_so < M:
    print(f"Hàng {hang_so}: {ma_tran[hang_so]}")
cot_so = int(input("số cột cần xem: "))
if 0 <= cot_so < N:
    cot = [ma_tran[i][cot_so] for i in range(M)]
    print(f"Cột {cot_so}: {cot}")
max_value = max(max(hang) for hang in ma_tran)
print(f"giá trị lớn nhất: {max_value}")