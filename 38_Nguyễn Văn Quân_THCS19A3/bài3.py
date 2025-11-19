tu = int(input("nhập tử số:"))
mau = int(input("nhập mẫu số:"))
if mau == 0:
    print("mẫu số không được bằng 0!")
else:
    a,b = abs(tu), abs(mau)
    while b != 0:
        a,b = b, a % b
    gcd = a
    tu_gon = tu // gcd
    mau_gon = mau // gcd
    print("phân số tối giản là:", tu_gon, "/", mau_gon)