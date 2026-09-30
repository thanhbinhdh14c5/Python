#hoatdong4
so_luot_truy_cap = 0 # bien global
def tang_luot_truy_cap():
 global so_luot_truy_cap
so_luot_truy_cap += 1
def vi_du_bien_local():
 so_luot_truy_cap = 100 # day la bien LOCAL, khac voi bien global cung ten
print("Ben trong ham, bien local =", so_luot_truy_cap)
tang_luot_truy_cap()
tang_luot_truy_cap()
print("So luot truy cap (global):", so_luot_truy_cap)
vi_du_bien_local()
print("Sau khi goi ham, bien global van la:", so_luot_truy_cap)

"""
 Yêu cầu: Giải thích vì sao nếu bỏ dòng global so_luot_truy_cap trong hàm tang_luot_truy_cap(), chương
trình sẽ báo lỗi UnboundLocalError.

 Trả lời: Nếu bỏ dòng global so_luot_truy_cap trong hàm tang_luot_truy_cap(), Python sẽ coi so_luot_truy_cap là một biến cục bộ (local) trong hàm. 
 Khi thực hiện phép tăng giá trị so_luot_truy_cap += 1, Python sẽ cố gắng truy cập biến cục bộ này trước khi nó được khởi tạo, dẫn đến lỗi 
 UnboundLocalError. 
 Việc khai báo global cho biến cho phép hàm biết rằng nó đang làm việc với biến toàn cục (global) thay vì tạo ra một biến cục bộ mới.

"""
#hoatdong5
#Bài tập 5.1 – map() với lambda:
danh_sach_so = [1, 2, 3, 4, 5]
binh_phuong = list(map(lambda x: x ** 2, danh_sach_so))
print(binh_phuong)

#Bài tập 5.2 – filter() với lambda:
so_chan = list(filter(lambda x: x % 2 == 0, danh_sach_so))
print(so_chan)

#Bài tập 5.3 – sorted() với lambda: sắp xếp danh sách sinh viên theo điểm:
danh_sach_sv = [
{"ten": "An", "diem": 8.5},

{"ten": "Binh", "diem": 7.0},
{"ten": "Chi", "diem": 9.2},
]
sap_xep_theo_diem = sorted(danh_sach_sv, key=lambda sv: sv["diem"])
sap_xep_giam_dan = sorted(danh_sach_sv, key=lambda sv: sv["diem"], reverse=True)
for sv in sap_xep_theo_diem:
 print(sv["ten"], "-", sv["diem"])
print("--- Giam dan ---")
for sv in sap_xep_giam_dan:
 print(sv["ten"], "-", sv["diem"])

""" Yêu cầu: So sánh cách sắp xếp này với cách "đặt điểm trước tên trong tuple" đã dùng ở Buổi 3 — vì sao
dùng key=lambda linh hoạt hơn?

 Trả lời: Dùng key=lambda linh hoạt hơn vì nó cho phép bạn chỉ định một hàm để trích xuất giá trị cần so sánh từ mỗi phần tử trong danh sách,
   mà không cần phải thay đổi cấu trúc dữ liệu gốc. Điều này giúp mã nguồn dễ đọc và dễ bảo trì hơn, đặc biệt khi bạn có nhiều điều kiện 
   sắp xếp phức tạp.
"""