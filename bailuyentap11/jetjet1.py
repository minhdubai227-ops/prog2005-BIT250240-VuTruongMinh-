strings = []
for i in range(5):
    s = input(f"chuoi {i+1}: ")
    strings.append(s)
print("\nket qua sap xep")
for i in range(1, len(strings)):
    key = strings[i]
    j = i - 1
    while j >= 0 and len(strings[j]) < len(key):
        strings[j + 1] = strings[j]
        j -= 1
    strings[j + 1] = key
    print(f"Bước {i}: {strings}")