password = ""
correct_password = "minhdeptrai"
while password != correct_password:
    password = input("Nhập mật khẩu: ")
    if password != correct_password:
        print("Mật khẩu sai, vui lòng thử lại.")
print("Đăng nhập thành công!")