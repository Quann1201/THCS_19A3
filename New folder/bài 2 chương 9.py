def giai_phuong_trinh_bac_nhat(a, b):
    if a == 0:
        if b == 0:
            print("Phuong trinh vo so nghiem")
        else:
            print("Phuong trinh vo nghiem")
    else:
        x = -b / a
        print("Nghiem cua phuong trinh la x =", x)

a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
giai_phuong_trinh_bac_nhat(a, b)
