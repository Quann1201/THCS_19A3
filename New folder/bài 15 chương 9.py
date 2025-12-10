def so_nguyen_to(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n=int(input("nhap so nguyen duong n:"))
if so_nguyen_to(n):
    print(n,"la so nguyen to")
else:
    print(n,"khong phai la so nguyen to")

print("cac so nguyen to trong khoang [100, 500]:")
for x in range(100,501):
    if so_nguyen_to(x):
        print(x,end="")