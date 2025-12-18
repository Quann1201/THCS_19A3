n=int(input("nhập số phần tử của danh sách:"))
a=[]
for i in range(n):
    x=int(input("nhập phần tử thứ{i+1}:"))
    a.append(x)

tong_chan=0
tong_le=0
for x in a:
    if x % 2 == 0:
        tong_chan += x
    else:
        tong_le += x

print("tổng các số chẵn:", tong_chan)
print("tổng các số lẻ:",tong_le)