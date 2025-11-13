nam = int(input("Nhập năm: "))
nam_nhuan = (nam % 400 == 0) or ((nam % 4 == 0) and (nam % 100 != 0))
print("Năm nhuận" * nam_nhuan or "Không phải năm nhuận")