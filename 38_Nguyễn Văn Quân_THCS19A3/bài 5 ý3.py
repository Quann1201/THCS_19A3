n = int(input("Nhập n: "))
S3 = 0
for i in range(1, n + 1):
    S3 += ((-1)**(i+1)) * (1/i)
print("S3 =", S3)
