from pathlib import Path

import pandas as pd

du_lieu = Path(__file__).resolve().parent / "diem_sinh_vien.csv"
df = pd.read_csv(du_lieu)
mon_hoc = ["Toan", "Ly", "Hoa"]

print(df.head())
print(df.shape)
print(df.columns.tolist())

# Bài tập 2.2 – Thống kê theo môn học:
diem_trung_binh_mon = df[mon_hoc].mean()
print(diem_trung_binh_mon)
print("Diem trung binh toan bo:", df[mon_hoc].mean().mean())
print("Diem cao nhat:", df[mon_hoc].max().max())
print("Diem thap nhat:", df[mon_hoc].min().min())

# Bài tập 2.3 – Tính DTB từng sinh viên & lọc đạt/không đạt:
diem_tb_sv = df.set_index("HoTen")[mon_hoc].mean(axis=1).round(2)
print(diem_tb_sv)
sinh_vien_dat = diem_tb_sv[diem_tb_sv >= 5.0]
sinh_vien_khong_dat = diem_tb_sv[diem_tb_sv < 5.0]
print("\nSinh vien dat:")
print(sinh_vien_dat)
print("\nSinh vien khong dat:")
print(sinh_vien_khong_dat)