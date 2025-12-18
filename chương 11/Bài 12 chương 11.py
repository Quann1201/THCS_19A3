# Nhập kích thước ma trận A
n = int(input("Nhập số hàng của ma trận A: "))
m = int(input("Nhập số cột của ma trận A: "))

A = []
for i in range(n):
    dong = []
    for j in range(m):
        x = int(input(f"Nhập A[{i}][{j}]: "))
        dong.append(x)
    A.append(dong)

# Nhập kích thước ma trận B
p = int(input("Nhập số hàng của ma trận B: "))
q = int(input("Nhập số cột của ma trận B: "))

B = []
for i in range(p):
    dong = []
    for j in range(q):
        x = int(input(f"Nhập B[{i}][{j}]: "))
        dong.append(x)
    B.append(dong)

# Kiểm tra điều kiện nhân ma trận
if m != p:
    print("Không thể nhân hai ma trận (số cột A ≠ số hàng B)")
else:
    # Khởi tạo ma trận kết quả C (n × q)
    C = []
    for i in range(n):
        dong = []
        for j in range(q):
            dong.append(0)
        C.append(dong)

    # Thực hiện phép nhân ma trận
    for i in range(n):
        for j in range(q):
            tong = 0
            for k in range(m):
                tong += A[i][k] * B[k][j]
            C[i][j] = tong

    # In ma trận kết quả
    print("Ma trận kết quả C = A × B:")
    for i in range(n):
        for j in range(q):
            print(C[i][j], end=" ")
        print()
