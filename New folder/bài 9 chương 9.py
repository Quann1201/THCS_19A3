def tinh_tong_chu_so(n):
    if n < 10:
        return n
    else:
        return (n % 10) + tinh_tong_chu_so(n//10)
    
n=int(input("nhap so nguyen duong n:"))
print("tong cac chu so la:", tinh_tong_chu_so(n))
