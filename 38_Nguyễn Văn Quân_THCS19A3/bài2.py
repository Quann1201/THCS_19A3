a = int(input("nhập số thứ nhất:"))
b = int(input("nhập số thứ hai:"))
while b != 0:
    a,b =b,a % b
    print("ước chung lớn nhất là:",a)