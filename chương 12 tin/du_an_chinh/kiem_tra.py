import sys
import os

# Lấy đường dẫn tuyệt đối tới thư mục thu_vien_chung
thu_vien_path = os.path.abspath("../thu_vien_chung")

# Thêm vào sys.path
sys.path.append(thu_vien_path)

# Import module
import xu_ly_so

# Gọi hàm kiểm tra số nguyên tố
so = 17
if xu_ly_so.kiem_tra_so_nguyen_to(so):
    print(so, "là số nguyên tố")
else:
    print(so, "không phải là số nguyên tố")
