from bai1_hinh_hoc import chu_vi_hinh_vuong, chu_vi_hinh_tron
from bai2_chuoi_utility import dao_nguoc_chuoi

cv_vuong = chu_vi_hinh_vuong(5)
cv_tron = chu_vi_hinh_tron(3)

chuoi = "Python rat de hoc"
ket_qua = dao_nguoc_chuoi(chuoi)

print("Chu vi hình vuông cạnh 5 là:", cv_vuong)
print("Chu vi hình tròn bán kính 3 là:", cv_tron)

print("Chuỗi ban đầu:", chuoi)
print("Chuỗi sau khi đảo ngược:", ket_qua)