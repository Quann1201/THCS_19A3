s=input("nhập chuỗi:")
ket_qua=""
la_khoang_trang= False # đánh dấu ký tự trước có phải dấu cách không

for ch in s:
    if ch != ' ':
        ket_qua= ket_qua + ch
        la_khoang_trang = False
    else:
        if la_khoang_trang == False:
            ket_qua=ket_qua + ch
            la_khoang_trang = True

# loại bỏ dấu cách ở cuối(nếu có)
if ket_qua != "" and ket_qua[-1] == ' ':
    ket_qua = ket_qua[:-1]

print("chuỗi sau khi xóa khoảng trắng thừa:")
print(ket_qua)