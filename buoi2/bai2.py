"""
Chú thích/docstring nhiều dòng:
Chương trình quản lý điểm sinh viên - Buổi 2
Tác giả: Lớp học Python
Ngày tạo: 2026
"""

# Chú thích một dòng: Khai báo và khởi tạo thông tin sinh viên
ho_ten = "Tran Thi B"  # Chú thích inline: Biến lưu họ tên sinh viên
ma_sv = "SV001"  # Chú thích inline: Biến lưu mã số sinh viên
diem_tb = 8.5  # Chú thích inline: Biến lưu điểm trung bình
#bai2-2

s1 = 'Xin chao'
s2 = "Ban co khoe khong?"
s3 = '''Day la
mot chuoi
nhieu dong'''
s4 = "Duong dan: C:\\Python\\data"
s5 = r"Duong dan raw: C:\Python\data"
s6 = "Toi ten la \"Nam\", con ban ten gi?"
print(s1); print(s2); print(s3); print(s4); print(s5); print(s6)
"""
Yêu cầu: giải thích khác biệt giữa s4 và s5 (raw string dùng khi nào?).
tra loi: S4 là một chuỗi thông thường, trong đó các ký tự đặc biệt như dấu gạch chéo ngược (\) được sử dụng để thoát ký tự tiếp theo. Do đó, để biểu diễn một đường dẫn trong Windows, bạn cần phải sử dụng hai dấu gạch chéo ngược (\\) để tránh lỗi cú pháp. Trong khi đó, S5 là một raw string (chuỗi thô), được định nghĩa bằng cách thêm tiền tố 'r' trước chuỗi. Trong raw string, các ký tự đặc biệt không được xử lý và được giữ nguyên, do đó bạn có thể viết đường dẫn trực tiếp mà không cần thoát ký tự. Raw string thường được sử dụng khi làm việc với các đường dẫn tệp hoặc biểu thức chính quy (regular expressions) để tránh việc phải thoát nhiều ký tự đặc biệt.
"""