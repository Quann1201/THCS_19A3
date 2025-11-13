# nhập dữ liệu từ bàn phím
day = float(input("nhập độ dài cạnh đáy (cm):"))
chieu_cao = float(input("nhập chiều cao (cm):"))
# tính diện tích hình tam giác
dien_tich = (day * chieu_cao)/2
# in kết quả
print(f" diện tích tam giác là: {dien_tich:.2f}")