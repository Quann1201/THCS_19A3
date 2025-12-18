n = int(input("Nhập số phần tử của tập A: "))
A = set()
for i in range(n):
    x = int(input(f"Nhập phần tử A[{i+1}]: "))
    A.add(x)

m = int(input("Nhập số phần tử của tập B: "))
B = set()
for i in range(m):
    x = int(input(f"Nhập phần tử B[{i+1}]: "))
    B.add(x)

# A - B
hieu_A_B = set()
for x in A:
    if x not in B:
        hieu_A_B.add(x)

# B - A
hieu_B_A = set()
for x in B:
    if x not in A:
        hieu_B_A.add(x)

# A giao B
giao = set()
for x in A:
    if x in B:
        giao.add(x)

# A hợp B
hop = set()
for x in A:
    hop.add(x)
for x in B:
    hop.add(x)

print("A - B:", hieu_A_B)
print("B - A:", hieu_B_A)
print("A giao B:", giao)
print("A hop B:", hop)
