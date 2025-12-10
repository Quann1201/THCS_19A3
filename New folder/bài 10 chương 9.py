def tim_so_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return tim_so_fibonacci(n-1) + tim_so_fibonacci(n-2)

n=int(input("nhap n:"))
print("so fibonacci thu", n ,"la", tim_so_fibonacci(n) )