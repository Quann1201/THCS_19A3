n=int(input("nhập số phần tử danh sách:"))
a=[]
for i in range(n):
    x=int(input("nhập phần tử thứ {i+1}:"))
    a.append(x)

k=int(input("nhập số vị trí cần dịch sang phải:"))
# tránh dịch thừa
if n != 0:
    k=k % n

for _ in range(k):
    cuoi=a[n-1] # lưu phần tử cuối

    i=n-1
    while i > 0:
        a[i]=a[i-1] # dịch sang phải
        i -= 1
    a[0]=cuoi # đưa phần tử cuối lên đầu 
print("danh sách sau khi dịch sang phải:") 
print(a)

