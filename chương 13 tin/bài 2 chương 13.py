with open("vanban.txt", "r", encoding="utf-8") as f:
    noi_dung = f.read()
ds_tu = noi_dung.split()
tan_suat = {}

for tu in ds_tu:
    if tu in tan_suat:
        tan_suat[tu] += 1
    else:
        tan_suat[tu] = 1

print("Tần suất xuất hiện của các từ trong tập tin:\n")
for tu, so_lan in tan_suat.items():
    print(f"Từ '{tu}': {so_lan} lần")
