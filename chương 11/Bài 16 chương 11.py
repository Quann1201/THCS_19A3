s = input("Nhập chuỗi: ")

tan_suat = {}

for ch in s:
    if ch in tan_suat:
        tan_suat[ch] = tan_suat[ch] + 1
    else:
        tan_suat[ch] = 1

print("Tần suất xuất hiện của các ký tự:")
for k in tan_suat:
    print(k, ":", tan_suat[k])
