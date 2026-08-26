

#Bài4.1
cau = "Lap trinh Python rat thu vi"
print(cau[0]) # ky tu dau tien
print(cau[-1]) # ky tu cuoi cung
print(cau[4:10]) # cat tu vi tri 4 den truoc vi tri 10
print(cau[:8]) # tu dau den vi tri 8
print(cau[11:]) # tu vi tri 11 den het
print(cau[::-1]) # dao nguoc chuoi

#Bai4.2

ten = "Nam"
# Thu gan lai mot ky tu: ten[0] = "T" -> quan sat loi TypeError
ten_moi = "T" + ten[1:]
print(ten_moi)

#Bai4.3
cau = " Toi dang HOC Python rat vui "
print(cau.strip()) # bo khoang trang 2 dau
print(cau.strip().upper()) # in hoa toan bo
print(cau.strip().lower()) # in thuong toan bo
print(cau.strip().replace("HOC", "hoc"))
print(cau.strip().split()) # tach thanh danh sach cac tu
print(len(cau.strip().split())) # dem so tu trong cau
print(cau.count("o")) # dem so lan xuat hien ky tu 'o'
print(cau.find("Python")) # vi tri bat dau cua "Python"
print(cau.strip().startswith("Toi"))
print(cau.strip().endswith("vui"))
print("-".join(["Python", "that", "thu", "vi"]))

#Bai4.4

ho_ten_tho = " nguyen van an "
ho_ten_sach = " ".join(ho_ten_tho.split()).title()
print(ho_ten_sach) # Nguyen Van An
ho_ten = input("Nhap ho ten: ")
sdt = input("Nhap so dien thoai: ")
email = input("Nhap email: ")
