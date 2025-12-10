def tim_so_le_lon_nhat(a,b,c):
    # tạo danh sách rỗng để lưu số lẻ
    so_le = []
    # kiểm tra từng số, nếu là số lẻ thì thêm vào danh sách
    if a % 2 != 0:
        so_le.append(a)
    if b % 2 != 0:
        so_le.append(b)
    if c % 2 != 0:
        so_le.append(c)
    # nếu danh sách không có số nào thì trả về -1
    if len(so_le)  == 0:
        return -1
    # trả về số lớn nhất trong các số lẻ
    return max(so_le)

a=int(input("nhap a:"))
b=int(input("nhap b:"))
c=int(input("nhap c:"))
print("so le lon nhat", tim_so_le_lon_nhat(a,b,c))