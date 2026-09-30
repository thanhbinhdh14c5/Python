def uscln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def bscnn(a, b):
    return a * b // uscln(a, b)

def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # tối ưu kiểm tra đến căn bậc 2
        if n % i == 0:
            return False
    return True

def kiem_tra_so_hoan_thien(n):
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n

# Kiểm tra các hàm
print(uscln(24, 36))          # 12
print(bscnn(4, 6))            # 12
print(kiem_tra_nguyen_to(29)) # True
print(kiem_tra_so_hoan_thien(28)) # True (28 là số hoàn thiện)

# Bài tập 1.2 – return không giá trị và trả về nhiều giá trị
def in_loi_chao(ten):
    print(f"Xin chào, {ten}!")
    return  # hàm không trả về giá trị (trả về None)

def chia_lay_thuong_du(a, b):
    return a // b, a % b  # trả về nhiều giá trị qua tuple

# Gọi hàm
in_loi_chao("An")
thuong, du = chia_lay_thuong_du(17, 5)
print(f"Thương: {thuong}, Dư: {du}")

#hoatdong2
def gioi_thieu(ten, tuoi=18, lop="Chua ro"):
 print(f"Ten: {ten} - Tuoi: {tuoi} - Lop: {lop}")
gioi_thieu("An") # dung het gia tri mac dinh
gioi_thieu("Binh", 20) # ghi de tuoi
gioi_thieu("Chi", lop="CNTT01") # dung tham so tu khoa, bo qua tuoi
gioi_thieu(ten="Dung", lop="CNTT02", tuoi=19) # thu tu tham so tu khoa co the dao lon
"""
yeu cau:Giải thích vì sao khi gọi hàm bằng tham số từ khóa (ten=..., lop=...) thì thứ tự truyền vào không
quan trọng.
tra loi: khi gọi hàm bằng tham số từ khóa, Python sẽ xác định giá trị của các tham số dựa trên tên của chúng thay vì vị trí.
 Do đó, bạn có thể truyền các tham số theo bất kỳ thứ tự nào miễn là bạn chỉ định đúng tên tham số.
 Điều này giúp tăng tính linh hoạt và rõ ràng trong việc gọi hàm, đặc biệt khi một hàm có nhiều tham số hoặc khi bạn muốn bỏ qua một số tham số 
 mà vẫn muốn cung cấp giá trị cho những tham số khác.

"""
#hoatdong3
#Bài tập 3.1 – *args: tính tổng số lượng bất kỳ các số:
def tinh_tong(*args):
   tong = 0
   for so in args:
       tong += so
   return tong

print(tinh_tong(1, 2, 3))
print(tinh_tong(5, 10, 15, 20, 25))
print(tinh_tong()) # khong truyen so nao -> tra ve 0

#Bài tập 3.2 – **kwargs: in thông tin động:
def in_thong_tin(ho_ten, tuoi, **kwargs):
    print(f"Ho ten: {ho_ten} - Tuoi: {tuoi}")
    for khoa, gia_tri in kwargs.items():
        print(f" {khoa}: {gia_tri}")

in_thong_tin("Nguyen Van A", 20, lop="CNTT01", que_quan="Ha Noi")
in_thong_tin("Tran Thi B", 21, email="b@example.com")