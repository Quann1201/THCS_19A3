# nhập dữ liệu từ bàn phím
tong_keo = int(input("nhập tổng số kẹo:"))
so_hoc_sinh = int(input("nhập số học sinh:"))
# tính toán
# phép chia lấy nguyên
keo_moi_hs = tong_keo // so_hoc_sinh
# phép chia lấy dư 
keo_con_thua = tong_keo % so_hoc_sinh 
# in kết quả
print(f" mỗi học sinh nhận được: {keo_moi_hs} cái kẹo")
print(f" số kẹo còn thừa: {keo_con_thua} cái kẹo")