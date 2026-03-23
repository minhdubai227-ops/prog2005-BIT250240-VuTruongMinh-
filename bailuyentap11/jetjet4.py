def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
numbers = [3,36,1,18,22,13,7]
print(f"ban dau{numbers}")
numbers.append(84764576847974749876548765987)
print(f"them{numbers}")
k = int(input("k"))
print(f"so{k} xuat hien {numbers.count(k)}lan")
prime_sum = 0
for num in numbers:
    if is_prime(num):
        prime_sum += num
print(f"tong cac so nguyen{prime_sum}")
numbers.sort()
print(f"sap xep{numbers}")
numbers.clear()
print(f"bi xoa{numbers}")