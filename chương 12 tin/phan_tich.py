from bai4_du_lieu.danh_sach import sap_xep_tang_dan
from bai4_du_lieu.tu_dien import lay_gia_tri

ds = [5, 2, 9, 1, 7]
tu_dien = {
    "a": 10,
    "b": 20,
    "c": 30
}

ds_sap_xep = sap_xep_tang_dan(ds)
gia_tri = lay_gia_tri(tu_dien, "b")

print("Danh sách ban đầu:", ds)
print("Danh sách sau khi sắp xếp:", ds_sap_xep)
print("Giá trị của khóa 'b':", gia_tri)
