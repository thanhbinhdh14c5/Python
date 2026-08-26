ho_ten =input("Nhập họ và tên: ")
nam_sinh = input("Nhập năm sinh: ")
diem_tb = float(input("Nhập điểm trung bình: "))
"""
yeu cau: giai thich vi sao phai ep kieu int()/float() cho nam_sinh va diem_tb
Khi người dùng nhập dữ liệu từ bàn phím bằng hàm input(), dữ liệu được trả về dưới dạng chuỗi (string) mặc định. Do đó, nếu bạn muốn sử dụng dữ liệu này cho các phép toán số học hoặc so sánh số học, bạn cần phải chuyển đổi (ép kiểu) dữ liệu từ chuỗi sang kiểu số thích hợp.
"""
# bai1-2
print("Python", "la", "ngon", "ngu", "lap trinh", sep="-")
print("Dong 1", end=" | ")
print("Dong 2")
"""
Yêu cầu: thử đổi sep thành nhiều ký tự khác nhau (", ",
"\n") và quan sát kết quả rồi giải thích.
tra loi:tham so sep trong hàm print() được sử dụng để xác định ký tự hoặc chuỗi ký tự sẽ được chèn giữa các đối số khi in ra. Khi bạn thay đổi giá trị của sep, kết quả in ra sẽ khác nhau tùy thuộc vào ký tự hoặc chuỗi bạn chọn. Ví dụ:
- Nếu bạn đặt sep=", ", các từ sẽ được phân tách bằng dấu phẩy và khoảng trắng.
- Nếu bạn đặt sep="\n", mỗi từ sẽ được in trên một dòng mới.

"""
# bai1-3
f-string
print(f"Ho ten: {ho_ten} - Nam sinh: {nam_sinh} - DTB: {diem_tb:.2f}")
# str.format()
print("Ho ten: {} - Nam sinh: {} - DTB: {:.2f}".format(ho_ten, nam_sinh, diem_tb))
# toán tử %
print("Ho ten: %s - Nam sinh: %d - DTB: %.2f" % (ho_ten, nam_sinh, diem_tb))
"""
Thảo luận: 3 cách trên cho kết quả giống nhau, vậy vì sao Python hiện nay khuyến khích dùng f-string
Tra loi: Python hiện nay khuyến khích sử dụng f-string vì nó cung cấp cú pháp ngắn gọn, dễ đọc và hiệu quả hơn so với các phương pháp cũ như str.format() và toán tử %. F-string cho phép bạn nhúng trực tiếp các biểu thức Python vào trong chuỗi bằng cách sử dụng dấu ngoặc nhọn {}, giúp mã nguồn trở nên rõ ràng và dễ hiểu hơn. Ngoài ra, f-string cũng hỗ trợ định dạng số và chuỗi một cách trực tiếp, làm cho việc hiển thị dữ liệu trở nên thuận tiện hơn.
"""
# 