while True:
    print("\n" + "=" * 30)
    print("MENU")
    print("1.Câu 1")
    print("2.Câu 2")
    print("3.Câu 3")
    print("4.Câu 4")
    print("5.Thoát")
    chon = input("Chọn (1-5): ")
    if chon == '1':
        a, b, c = 3, 5, 7
        print(f"Min = {min(a, b, c)}, Max = {max(a, b, c)}")
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            print("pt vo nghiem")
        elif delta == 0:
            print(f"nghiem kep: x = {-b / (2 * a)}")
        else:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            print(f"x1 = {x1:.2f}, x2 = {x2:.2f}")
    elif chon == '2':
        print("Số lẻ giảm dần:")
        for i in range(111, 16, -2): print(i, end=" ")
        print("\nSố nguyên tố:")
        for i in range(17, 112):
            if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1)) and i > 1:
                print(i, end=" ")
    elif chon == '4':
        n = int(input("Nhap N: "))
        a = [int(input(f"a[{i}] = ")) for i in range(n)]
        for i in range(n - 1):
            m = i
            for j in range(i + 1, n):
                if a[j] > a[m]: m = j
            a[i], a[m] = a[m], a[i]
            print(f"Buoc {i + 1}: {a}")
        print("Ket qua:", a)
    elif chon == '5':
        print("Bye!")
    else:
        print("chọn lại đi nhóc!")