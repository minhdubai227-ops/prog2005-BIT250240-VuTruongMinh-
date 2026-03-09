print("Số lẻ từ 17 đến 111 giảm dần:")
for i in range(111, 16, -2):
    print(i, end=" ")
print("\n\nSố nguyên tố từ 17 đến 111:")
def is_prime(n):
    if n<2: return False
    for i in range(2,int(n*0.5)+ 1):
     if n % i == 0: return False
    return True
for i in range(17, 112):
    if is_prime(i):
     print(i, end=" ")