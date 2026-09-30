# hoatdong6
# Bài tập 6.1 – Giai thừa bằng đệ quy
"""Yêu cầu: Sau khi thực hiện bằng đệ quy, hãy so sánh với vòng lặp.
   Tra loi: Khi tính giai thừa bằng đệ quy, mỗi lời gọi hàm tạo ra một khung ngăn xếp mới trong bộ nhớ, 
   dẫn đến việc sử dụng bộ nhớ nhiều hơn và có thể gây ra lỗi tràn ngăn xếp (stack overflow) nếu n quá lớn.
   Trong khi đó, vòng lặp chỉ sử dụng một khung ngăn xếp duy nhất và thực hiện các phép tính trong cùng một không gian bộ nhớ, 
   do đó hiệu quả hơn về mặt bộ nhớ và tốc độ thực thi.
"""
def giai_thua_de_quy(n):
   if n <= 1:  # dieu kien dung
      return 1
   return n * giai_thua_de_quy(n - 1)
def giai_thua_lap(n):
   ket_qua = 1
   for i in range(1, n + 1):
      ket_qua *= i
   return ket_qua
print(giai_thua_de_quy(5), "-", giai_thua_lap(5))

# Bài tập 6.2 – Số Fibonacci thứ n bằng đệ quy:
def fibonacci_de_quy(n):
   if n <= 1:  # dieu kien dung
      return n
   return fibonacci_de_quy(n - 1) + fibonacci_de_quy(n - 2)


for i in range(10):
   print(fibonacci_de_quy(i), end=" ")
print()

""""Yêu cầu: Thử tính fibonacci_de_quy(30). Đệ quy Fibonacci tốn kém hơn vì
 số lần gọi hàm tăng theo cấp số nhân, do tính lại nhiều lần các giá trị trùng nhau.
 tra loi: Khi tính fibonacci_de_quy(30), số lượng các lời gọi hàm tăng lên rất nhanh, dẫn đến thời gian thực thi lâu và tốn nhiều bộ nhớ.
 Trong khi đó, vòng lặp chỉ cần duyệt qua các giá trị từ 0 đến n một lần, nên hiệu quả hơn nhiều. Đệ quy Fibonacci không tối ưu vì 
 nó tính lại các giá trị đã được tính trước đó, trong khi vòng lặp chỉ tính một lần cho mỗi giá trị.
 """