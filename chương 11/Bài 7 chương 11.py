n=int(input("nhập số phần tử cả danh sách:"))
a=[]
for i in range(n):
    x=int(input("nhập phần tử thứ {i+1}:"))
    a.append(x)

k=int(input("nhập giá trị cần tìm(k):"))
co_cap=False
for i in range(n-1):
    for j in range(i+1, n):
        if a[i]+a[j] == k:
            print("cặp số:",a[i],a[j])
            co_cap = True

if co_cap == False:
    print("không có cặp số nào có tổng bằng", k)