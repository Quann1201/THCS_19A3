n = int(input(" nhập số n:"))
if n < 0:
    print(" không phải số chính phương")
else:
    k = int(n**0.5)
    if k*k == n:
        print(n, " là số chính phương ")
    else:
        print(n, " không phải số chính phương")