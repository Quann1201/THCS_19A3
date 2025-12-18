n = int(input("Nhập số hàng của ma trận: "))
m = int(input("Nhập số cột của ma trận: "))
a = []
for i in range(n):
    dong = []
    for j in range(m):
        x = int(input(f"Nhập a[{i}][{j}]: "))
        dong.append(x)
    a.append(dong)

hang_max = 0
tong_max = 0

for i in range(n):
    tong_hang = 0
    for j in range(m):
        tong_hang += a[i][j]
    if i == 0 or tong_hang > tong_max:
        tong_max = tong_hang
        hang_max = i
print("Hàng có tổng lớn nhất là hàng:", hang_max)
print("Tổng lớn nhất:", tong_max)
