# nhập dữ liệu từ bàn phím
can_nang = float(input(" nhập cân nặng (kg):"))
chieu_cao = float(input(" nhập chiều cao (m):"))
# tính BMI theo công thức
bmi = can_nang / (chieu_cao ** 2)
# in kết quả
print(f" chỉ số BMI của bạn là: {bmi:.2f}")