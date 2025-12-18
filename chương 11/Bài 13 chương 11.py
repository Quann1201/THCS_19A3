n = int(input("Nhập số hàng của ma trận: "))
m = int(input("Nhập số cột của ma trận: "))

a = []

for i in range(n):
    dong = []
    for j in range(m):
        x = int(input(f"Nhập a[{i}][{j}]: "))
        dong.append(x)
    a.append(dong)

# Kiểm tra ma trận vuông
if n != m:
    print("Ma trận KHÔNG phải là ma trận vuông nên KHÔNG phải ma trận đơn vị")
else:
    la_don_vi = True

    for i in range(n):
        for j in range(n):
            if i == j:
                if a[i][j] != 1:
                    la_don_vi = False
                    break
            else:
                if a[i][j] != 0:
                    la_don_vi = False
                    break
        if la_don_vi == False:
            break

    if la_don_vi:
        print("Ma trận là ma trận đơn vị")
    else:
        print("Ma trận KHÔNG phải là ma trận đơn vị")
