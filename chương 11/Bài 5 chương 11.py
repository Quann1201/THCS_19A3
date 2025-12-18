n=int(input("nhập số phần tử của danh sách:"))
a=[]
for i in range(n):
    x=int(input("nhập phần tử thứ {i+1}:"))
    a.append(x)
ket_qua= []

for x in a:
    da_ton_tai = False
    for y in ket_qua:
        if x == y:
            da_ton_tai = True
            break
    if da_ton_tai == False:
        ket_qua.append(x)

print("danh sách sau khi loại bỏ phần tử trùng lặp:")
print(ket_qua)