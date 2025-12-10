def kiem_tra_doi_xung(n):
    # chuyển n thành chuỗi để kiểm tra đọc xuôi và đọc ngược
    chuoi_n=str(n)
    # so sánh chuỗi bình thường và đảo ngược
    if chuoi_n== chuoi_n[::-1]:
        return True
    else:
        return False
    
n=int(input("nhap so nguyen duong n:"))
if kiem_tra_doi_xung(n):
    print(n,"la so doi xung")
else:
    print(n,"khong phai la so doi xung")