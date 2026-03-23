def nhap_ma_tran(hang, cot, ten):
    print(f"\nma tran {ten}:")
    mt = []
    for i in range(hang):
        while True:
            try:
                row = input(f"hag {i+1} (nhap {cot} ").strip()
                if not row:
                    raise ValueError("khong de trong")
                numbers = list(map(float, row.split()))
                if len(numbers) != cot:
                    print(f"nhap {cot} so")
                    continue
                mt.append(numbers)
                break
            except ValueError as e:
                print(f"loi {e}")
    return mt
hang = int(input("so hang "))
cot = int(input("so cot "))
mt1 = nhap_ma_tran(hang, cot, "A")
mt2 = nhap_ma_tran(hang, cot, "B")
ket_qua = [[mt1[i][j] + mt2[i][j] for j in range(cot)] for i in range(hang)]
print("\nkq")
for hang in ket_qua:
    print(hang)