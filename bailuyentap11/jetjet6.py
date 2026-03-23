n = int(input("so luong nguoi"))
people = {}
for i in range(n):
    name = input(f"nguoi thu {i+1}: ")
    age = int(input(f"tuoi cua {name}: "))
    people[name] = age
if n > 0:
    avg_age = sum(people.values()) / n
    print(f"\ntuoi tb{avg_age:.2f}")
    print(f"danh sach{people}")