so_nguyen = 15
so_thuc = 4.2
so_phuc = 3 + 4j
print(type(so_nguyen), type(so_thuc), type(so_phuc))
print(float(so_nguyen)) # ep int -> float
print(int(so_thuc)) # ep float -> int (cat phan thap phan)
#bai3-2
a = -7
b = 2.6789
c, d = 17, 5
print(abs(a)) # gia tri tuyet doi
print(round(b)) # lam tron
print(round(b, 2)) # lam tron 2 chu so thap phan
print(pow(c, 2)) # c mu 2
print(divmod(c, d)) # tra ve (thuong, du) dang tuple
"""
Yêu cầu: so sánh pow(c, 2) với c ** 2 (toán tử đã học ở Buổi 1) - hai cách này có luôn cho kết quả
giống nhau không? Tại sao?
tra loi: Cả hai cách pow(c, 2) và c ** 2 đều thực hiện phép lũy thừa, nhưng chúng có thể cho kết quả khác nhau trong một số trường hợp nhất định. Cụ thể:
- pow(c, 2) là một hàm tích hợp trong Python, có thể nhận
"""
   #bai3-3

a, b, c = 1, -3, 2
delta = b ** 2 - 4 * a * c
x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)
print(f"Delta = {delta}")
print(f"Nghiem x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")