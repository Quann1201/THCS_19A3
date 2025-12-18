n=int(input("nhập số phần tử của danh sách:"))

a=[]
for i in range(n):
    x=int(input("nhập phần tử thứ {i+1}:"))
    a.append(x)

# giả sử ban đầu
lon_nhat = a[0]
lon_hai = None

for i in range(1,n):
    if a[i] > lon_nhat:
        lon_hai = lon_nhat
        lon_nhat = a[i]
    elif a[i] < lon_nhat:
        if lon_hai is None or a[i] > lon_hai:
            lon_hai = a[i]

if lon_hai is None:
    print("không tồn tại giá trị thứ hai")
else:
    print("giá trị lớn thứ hai là:",lon_hai)