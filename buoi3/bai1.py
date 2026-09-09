diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]
print(diem_so[0]) # phan tu dau tien
print(diem_so[-1]) # phan tu cuoi cung
print(diem_so[1:4]) # cat tu vi tri 1 den truoc 4
print(diem_so[::2]) # lay cach 1 phan tu (step = 2)
print(diem_so[::-1]) # dao nguoc danh sach
# bai1.2
ten_sv = ["An", "Binh", "Chi"]
ten_sv.append("Dung") # them vao cuoi
ten_sv.insert(1, "Em") # chen vao vi tri 1
print(ten_sv)
ten_sv.remove("Chi") # xoa theo gia tri
pop_ra = ten_sv.pop() # xoa va lay ra phan tu cuoi
print(ten_sv, "- da xoa:", pop_ra)
ten_sv.sort() # sap xep tang dan (theo bang chu cai)
print(ten_sv)
ten_sv.reverse() # dao nguoc thu tu hien tai
print(ten_sv)
ten_sv.extend(["Giang", "Hoa"]) # noi them mot list khac vao
print(ten_sv)
"""
tra loi:su khac nhau giua remove va pop la:
- remove() xoa phan tu theo gia tri, neu co nhieu phan tu   giong nhau, chi xoa phan tu dau tien tim thay. Neu khong tim thay gia tri, se phat sinh loi.        

"""