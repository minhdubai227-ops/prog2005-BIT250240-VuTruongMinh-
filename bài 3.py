n = int(input("Nhập số lượng số Fibonacci cần in: "))
a, b = 0, 1
count = 0
print(f"{n} số đầu tiên của dãy Fibonacci:")
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1