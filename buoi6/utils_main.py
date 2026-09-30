def dao_nguoc_chuoi(chuoi):
 return chuoi[::-1]
def kiem_tra_palindrome(chuoi):
 return chuoi == chuoi[::-1]
def chuan_hoa_ho_ten(chuoi):
 return " ".join(chuoi.split()).title()
def uscln(a, b):
 while b != 0:
  a, b = b, a % b
 return a
def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

#File main.py:

if __name__ == "__main__":
    print(dao_nguoc_chuoi("Python"))
    print(kiem_tra_palindrome("madam"))
    print(chuan_hoa_ho_ten(" nguyen van an "))
    print(uscln(24, 36))
    print(kiem_tra_nguyen_to(29))

"""
Yêu cầu: Giải thích vì sao utils.py và main.py cần đặt trong cùng một thư mục để lệnh import utils hoạt động
đúng.
Trả lời: Khi sử dụng lệnh import utils trong main.py, Python sẽ tìm kiếm module utils.py trong các thư mục được liệt kê trong sys.path.
Nếu utils.py và main.py không nằm trong cùng một thư mục, Python sẽ không thể tìm thấy module utils và sẽ báo lỗi ModuleNotFoundError. 
Đặt chúng trong cùng một thư mục đảm bảo rằng Python có thể tìm thấy và import module utils thành công.

"""