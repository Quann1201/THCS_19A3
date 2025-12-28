import os

os.mkdir("temp_files")

# Tạo tập tin file.txt trong temp_files
with open("temp_files/file.txt", "w", encoding="utf-8") as f:
    f.write("Đây là tập tin tạm thời.")

# Đổi tên file.txt thành new_file.txt
os.rename("temp_files/file.txt", "temp_files/new_file.txt")

# Di chuyển new_file.txt ra thư mục hiện tại
os.rename("temp_files/new_file.txt", "new_file.txt")

# Xóa thư mục temp_files
os.rmdir("temp_files")

print(" Hoàn thành")
