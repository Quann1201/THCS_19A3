tien_vnd = float(input(" nhập số tiền (VNĐ):"))
# tỷ giá quy đổi
ty_gia = 24500
# tính số tiền usd
tien_usd = tien_vnd / ty_gia
print(f"số tiền tương ứng: {tien_usd:.2f} USD")