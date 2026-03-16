s = input("nhap de: ")
upper = lower = digit = special = space = vowel = 0
vowels = "ueoaiUEOAI"
for char in s:
    if char.isupper():
        upper += 1
    if char.islower():
        lower += 1
    if char.isdigit():
        digit += 1
    if char.isspace():
        space += 1
    if char in vowels:
        vowel += 1
special = len(s) - (upper + lower + digit + space)
print(f"chu in hoa: {upper}")
print(f"chu thuong: {lower}")
print(f"chu so: {digit}")
print(f"so ky tu: {special}")
print(f"khoang trang: {space}")
print(f"so nguyen am: {vowel}")