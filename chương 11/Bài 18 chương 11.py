n = int(input("Nhập số cặp key-value: "))

d = {}
for i in range(n):
    key = int(input(f"Nhập key thứ {i+1}: "))
    value = int(input(f"Nhập value tương ứng: "))
    d[key] = value

# Dictionary đảo
dao = {}

for k in d:
    v = d[k]
    dao[v] = k

print("Dictionary ban đầu:", d)
print("Dictionary sau khi đảo:", dao)
