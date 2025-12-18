n = int(input("Nhập cấp của ma trận vuông: "))

a = []
for i in range(n):
    dong = []
    for j in range(n):
        x = int(input(f"Nhập a[{i}][{j}]: "))
        dong.append(x)
    a.append(dong)

doi_xung = True

for i in range(n):
    for j in range(i + 1, n):
        if a[i][j] != a[j][i]:
            doi_xung = False
            break
    if doi_xung == False:
        break

if doi_xung:
    print("Ma trận là ma trận đối xứng")
else:
    print("Ma trận KHÔNG phải là ma trận đối xứng")
