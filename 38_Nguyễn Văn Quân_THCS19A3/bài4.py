# Hàm kiểm tra số nguyên tố
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
# Nhập n
n = int(input("Nhập n: "))
print("Các số nguyên tố nhỏ hơn", n, "là:")
for num in range(2, n):
    if is_prime(num):
        print(num, end=" ")