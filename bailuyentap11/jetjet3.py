numbers = list(map(int, input("nhap").split()))
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(f"cac so chan{even_numbers}")
print(f"tong cac so chan{sum(even_numbers)}")