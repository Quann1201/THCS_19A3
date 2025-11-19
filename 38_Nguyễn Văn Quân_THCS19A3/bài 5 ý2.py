n = int(input("Nhập n: "))
S2 = 1
for i in range(1, n):    # chạy đến n-1
    S2 *= i
print("S2 =", S2)
