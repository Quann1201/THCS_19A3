# nhập số tiền gửi và lãi suất hàng năm
tien_gui = float(input(" nhập số tiền ban đầu (VNĐ):"))
lai_suat_nam = float(input(" nhập lãi suất hàng năm (%):"))
# chuyển lãi suất từ % sang số thập phân
lai_suat = lai_suat_nam / 100
# tính lãi đơn theo thời gian
lai_1_thang = tien_gui * lai_suat / 12
lai_2_quy = tien_gui * lai_suat / 6
lai_3_nam = tien_gui * lai_suat * 3
# in kết quả
print(f"lãi nhận được sau 1 tháng: {lai_1_thang:.2f}VNĐ")
print(f"lãi nhận được sau 2 quý: {lai_2_quy:.2f}VNĐ")
print(f"lãi nhận được sau 3 năm: {lai_3_nam:.2f}VNĐ")