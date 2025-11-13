ten = input(" nhập tên đăng nhập:")
mk = input(" nhập mật khẩu:")
quyen_truy_cap = (ten == "admin")and (mk != "password123")
print(" truy cập thành công"* quyen_truy_cap or " truy cập thất bại")