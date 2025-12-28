with open("vanban.txt", "w", encoding="utf-8") as f:
    f.write(
        "Python là một ngôn ngữ lập trình mạnh mẽ, dễ học và có nhiều ứng dụng. "
        "Nó được sử dụng rộng rãi trong phát triển web, khoa học dữ liệu, trí tuệ "
        "nhân tạo và tự động hóa. Cộng đồng Python rất lớn và hỗ trợ tuyệt vời, "
        "với nhiều thư viện phong phú để giải quyết mọi vấn đề."
    )

with open("vanban.txt", "r", encoding="utf-8") as f:
    noi_dung = f.read()

ds_tu = noi_dung.split()
so_tu = len(ds_tu)

print("Nội dung tập tin:")
print(noi_dung)
print("\nTổng số từ trong tập tin là:", so_tu)