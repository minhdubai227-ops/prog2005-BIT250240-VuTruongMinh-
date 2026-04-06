students = {"minh":8,"manh":7,"thminh":9}
def diem_tb(dict_sv):
    return sum(dict_sv.values()) , len(dict_sv)
print(diem_tb(students))