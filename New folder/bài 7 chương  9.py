def la_so_hoan_hao(n):
    if n <=1:
        return False
    
    tong_uoc=0
    for i in range(1, n//2 +1):
        if n%i ==0:
            tong_uoc += i
    return tong_uoc == n

def tinh_tong_so_hoan_hao(a,b):
    tong = 0
    for num in range(a, b + 1):
        if la_so_hoan_hao(num):
            tong += num
    return tong

a=int(input("nhap a:"))
b=int(input("nhap b:"))
print("tong cac so hoan hao:", tinh_tong_so_hoan_hao(a,b))