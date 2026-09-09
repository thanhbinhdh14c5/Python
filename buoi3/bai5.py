import math
diem_a = (2, 3)
diem_b = (7, 8)
xa, ya = diem_a
xb, yb = diem_b

khoang_cach = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
print(f"Khoang cach giua {diem_a} va {diem_b} la: {round(khoang_cach, 2)}")

#Yêu cầu: tạo thêm danh sách cac_diem = [(0,0), (3,4), (6,8)] (list chứa các tuple tọa độ), dùng for để in ra khoảng cách của từng điểm so với gốc tọa độ (0, 0).

diem_c=(0, 0)
diem_d=(3, 4)
diem_e=(6, 8)
xc, yc = diem_c
xd, yd = diem_d
xe, ye = diem_e
khoang_cach_cd = math.sqrt((xd - xc) ** 2 + (yd - yc) ** 2)
khoang_cach_ce = math.sqrt((xe - xc) ** 2 + (ye - yc) ** 2)
print(f"Khoang cach giua {diem_c} va {diem_d} la: {round(khoang_cach_cd, 2)}")
print(f"Khoang cach giua {diem_c} va {diem_e} la: {round(khoang_cach_ce, 2)}")