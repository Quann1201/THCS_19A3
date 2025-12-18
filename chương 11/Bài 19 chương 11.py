n = int(input("Nhập số sinh viên: "))

sv = {}
for i in range(n):
    ten = input(f"Nhập tên sinh viên thứ {i+1}: ")
    diem = float(input(f"Nhập điểm của {ten}: "))
    sv[ten] = diem

# Dictionary nhóm theo điểm
nhom = {}

for ten in sv:
    diem = sv[ten]

    if diem in nhom:
        nhom[diem].append(ten)
    else:
        nhom[diem] = [ten]

print("Kết quả nhóm theo điểm:")
for d in nhom:
    print(d, ":", nhom[d])
