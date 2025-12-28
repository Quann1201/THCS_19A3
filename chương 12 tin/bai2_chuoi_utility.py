def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]

def dem_so_tu(chuoi):
    # tách chuỗi theo khoảng trắng và đếm số phần tử
    return len(chuoi.split())
