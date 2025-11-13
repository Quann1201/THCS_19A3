luong_co_ban = float(input("Nhập lương cơ bản: "))
ngay_cong = int(input("Nhập số ngày công trong tháng: "))
# Lương 1 ngày
luong_ngay = luong_co_ban / 22
# Tiền lương gốc theo ngày làm việc
luong = luong_ngay * ngay_cong
# Thưởng 10% nếu > 22 ngày, phạt 5% nếu < 22 ngày
thuong = luong * 0.10 * (ngay_cong > 22)
phat   = luong * 0.05 * (ngay_cong < 22)
# Lương thực nhận
tong_luong = luong + thuong - phat
print("Tổng lương thực nhận là:", tong_luong, "VNĐ")
