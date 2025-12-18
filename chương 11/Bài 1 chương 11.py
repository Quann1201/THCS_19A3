s=input("nhập chuỗi:")
chu_cai=0
chu_so=0
ky_tu_dac_biet=0
for ch in s:
    if('a'<=ch<='z') or ('A'<=ch<="Z"):
        chu_cai +=1
    elif'0'<=ch<='9':
        chu_so +=1
    else:
        ky_tu_dac_biet +=1
print("số ký tự chữ cái", chu_cai)
print("số ký tự chữ số", chu_so)
print("số ký tự đặc biệt",ky_tu_dac_biet)