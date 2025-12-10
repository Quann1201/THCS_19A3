def la_so_nguyen_to(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def in_so_nguyen_to_trong_khoang(a,b):
    print(f"cac so nguyen to trong khoang tu {a} den {b}:")
    for num in range(a,b +1):
        if la_so_nguyen_to(num):
            print(num, end="")
    print()

a=int(input("nhap a:"))
b=int(input("nhap b:"))
in_so_nguyen_to_trong_khoang(a,b)