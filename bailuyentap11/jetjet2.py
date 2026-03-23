strings = []
for i in range(5):
    s = input(f"chuoi {i+1}: ")
    strings.append(s)
for i in range(1, len(strings)):
    key = strings[i]
    j = i - 1
    while j >= 0 and len(strings[j]) < len(key):
        strings[j + 1] = strings[j]
        j -= 1
    strings[j + 1] = key
search = input("\nchuoi can tim")
left, right = 0, len(strings) - 1
found = False
while left <= right:
    mid = (left + right) // 2
    if strings[mid] == search:
        print(f"tim thay'{search}' tai vi tri' {mid}'")
        found = True
        break
    elif strings[mid] < search:
        left = mid + 1
    else:
        right = mid - 1
if not found:
    print(f"khong tim thay'{search}'")