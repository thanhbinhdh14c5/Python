diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]
tong = 0
for diem in diem_so:
    print(diem)
tong = tong + diem
print("Tong diem:", tong)
print("Diem trung binh:", round(tong / len(diem_so), 2))
ma_tran = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
# In ra theo tung hang
for hang in ma_tran:
    print(hang)
# In ra tung phan tu, duyet theo hang roi theo cot
for hang in ma_tran:
 for phan_tu in hang:
  print(phan_tu, end=" ")
print()
"""
tra loi:dung bien tong qua hai vong for lap nhau
"""
#tinh tong cac phan tu trong ma tran
tong_ma_tran = 0
for hang in ma_tran:
    for phan_tu in hang:
        tong_ma_tran += phan_tu
        print(tong_ma_tran)
        

