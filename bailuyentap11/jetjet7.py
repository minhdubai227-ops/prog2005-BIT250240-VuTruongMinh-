import csv
name = input("ten")
age = input("tuoi")
emp_id = input("id")
with open("danhsachnhanvien", "w", encoding="utf-8") as f:
    f.write(f"Tên: {name}\ntuoi: {age}\nid: {emp_id}")
with open("thuviennhanvien", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["ten", "tuoi", "id"])
    writer.writerow([name, age, emp_id])
print("da luu vao file danhsachnhanvien va thuviennhanvien")