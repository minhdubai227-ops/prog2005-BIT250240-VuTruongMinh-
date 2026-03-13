def diem_trung_binh(sv_dict):
    return sum(sv_dict.values()) / len(sv_dict)
sv = {"minh": 9.9, "manh": 3, "thien minh": 4}
print(diem_trung_binh(sv))