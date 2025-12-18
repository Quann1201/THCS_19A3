n = int(input("Nhập số phần tử của tuple: "))

t = ()
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    t = t + (x,)

tuple_chan = ()
tuple_le = ()

tong_chan = 0
tong_le = 0

for x in t:
    if x % 2 == 0:
        tuple_chan = tuple_chan + (x,)
        tong_chan += x
    else:
        tuple_le = tuple_le + (x,)
        tong_le += x

print("Tuple ban đầu:", t)
print("Tuple các số chẵn:", tuple_chan)
print("Tổng các số chẵn:", tong_chan)
print("Tuple các số lẻ:", tuple_le)
print("Tổng các số lẻ:", tong_le)
