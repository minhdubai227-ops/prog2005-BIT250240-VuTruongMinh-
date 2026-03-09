n = int(input("Nhập N: "))
a = []
for i in range(n):
    a.append(int(input(f"a[{i}] = ")))
print("Quá trình sắp xếp:")
for i in range(n-1):
    max_idx = i
    for j in range(i+1, n):
        if a[j] > a[max_idx]:
            max_idx = j
    a[i], a[max_idx] = a[max_idx], a[i]
    print(f"Bước {i+1}: {a}")
print("Kết quả cuối:", a)