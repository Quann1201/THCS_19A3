tep_nguon = "nguon.dat"
tep_dich = "ban_sao.dat"

with open(tep_nguon, "rb") as f_nguon, open(tep_dich, "wb") as f_dich:
    while True:
        du_lieu = f_nguon.read(1024)  # Đọc 1024 byte mỗi lần
        if not du_lieu:
            break
        f_dich.write(du_lieu)

print("Đã sao chép tập tin thành công!")
