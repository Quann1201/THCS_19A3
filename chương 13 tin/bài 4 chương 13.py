with open("san_pham.txt", "w", encoding="utf-8") as f:
    f.write("ID, Tên sản phẩm, Giá\n")
    f.write("1, Laptop, 1200\n")
    f.write("2, Chuột máy tính, 25\n")
    f.write("3, Bàn phím, 75\n")

id_can_cap_nhat = input("Nhập ID sản phẩm cần cập nhật giá: ")
gia_moi = input("Nhập giá mới: ")

with open("san_pham.txt", "r", encoding="utf-8") as f:
    cac_dong = f.readlines()

danh_sach_moi = []

for dong in cac_dong:
    dong = dong.strip()
    # Bỏ qua dòng tiêu đề
    if dong.startswith("ID"):
        danh_sach_moi.append(dong)
        continue

    parts = dong.split(", ")
    if parts[0] == id_can_cap_nhat:
        # Cập nhật giá mới
        dong_moi = f"{parts[0]}, {parts[1]}, {gia_moi}"
        danh_sach_moi.append(dong_moi)
    else:
        danh_sach_moi.append(dong)

# Ghi đè lại tập tin
with open("san_pham.txt", "w", encoding="utf-8") as f:
    for dong in danh_sach_moi:
        f.write(dong + "\n")

print("Đã cập nhật giá sản phẩm thành công!")
