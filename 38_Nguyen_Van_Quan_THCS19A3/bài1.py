# nhập dữ liệu từ bàn phím
gia = float(input("nhập giá sản phẩm:"))
so_luong = int(input("nhập số lượng mua:"))
# tính toán
tong_chi_phi = gia * so_luong
thue_vat = tong_chi_phi * 0.10
tong_tien = tong_chi_phi + thue_vat
# in kết quả làm trong đến h2 chữ số thập phân
print(f"tổng chi phí: {tong_chi_phi:.2f}")
print(f"thuế VAT(10%): {thue_vat:.2f}")
print(f"tổng số tiền phải trả: {tong_tien:.2f}")
