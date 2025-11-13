kwh = int(input("Nhập số kWh điện đã tiêu thụ: "))
# Tính tiền theo các bậc
tien = (
    (kwh * 1678) * (kwh <= 100) +
    ((100 * 1678) + (kwh - 100) * 1734) * (100 < kwh <= 200) +
    ((100 * 1678) + (100 * 1734) + (kwh - 200) * 2014) * (200 < kwh <= 300)
)
print("Tổng tiền điện phải trả là:", tien, "VNĐ")
