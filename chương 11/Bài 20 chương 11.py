n = int(input("Nhập số cặp key-value: "))

d = {}
for i in range(n):
    key = input(f"Nhập key thứ {i+1}: ")
    value = int(input(f"Nhập value tương ứng: "))
    d[key] = value

# Dictionary lọc kết quả
loc = {}

for k in d:
    if d[k] > 50:
        loc[k] = d[k]

print("Dictionary ban đầu:", d)
print("Các cặp key-value có giá trị > 50:", loc)
