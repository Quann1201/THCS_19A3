n = int(input("Nhập số cặp key-value: "))

d = {}

for i in range(n):
    key = int(input(f"Nhập key thứ {i+1}: "))
    value = int(input(f"Nhập value tương ứng: "))
    d[key] = value

# Giả sử key đầu tiên có value lớn nhất
for k in d:
    key_max = k
    break

# So sánh các value còn lại
for k in d:
    if d[k] > d[key_max]:
        key_max = k

print("Key có giá trị lớn nhất là:", key_max)
print("Giá trị lớn nhất là:", d[key_max])
