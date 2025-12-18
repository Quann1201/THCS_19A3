n = int(input("Nhập cấp của ma trận vuông: "))

a = []
for i in range(n):
    dong = []
    for j in range(n):
        x = int(input(f"Nhập a[{i}][{j}]: "))
        dong.append(x)
    a.append(dong)

tong = 0
for i in range(n):
    tong += a[i][n - 1 - i]

print("Tổng các phần tử trên đường chéo phụ:", tong)
