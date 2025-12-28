import csv

with open("nhan_vien.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Tên", "Lương"])
    writer.writerow([1, "Nguyễn Văn A", 45000])
    writer.writerow([2, "Trần Thị B", 60000])
    writer.writerow([3, "Lê Văn C", 75000])
    writer.writerow([4, "Phạm Thị D", 50000])

with open("nhan_vien.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    print("Danh sách nhân viên có lương trên 50000:\n")
    for dong in reader:
        if int(dong["Lương"]) > 50000:
            print(f"ID: {dong['ID']}, Tên: {dong['Tên']}, Lương: {dong['Lương']}")
