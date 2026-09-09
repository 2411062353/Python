ten = "Nguyen Van A"
diem_toan = 8.5
diem_van = 7.0
so_luong_mon_hoc = 2
MUC_LUONG_TOI_THIEU = 5000000  # Hằng số viết hoa toàn bộ

print("Họ và tên:", ten)
print("Điểm Toán:", diem_toan)
print("Điểm Văn:", diem_van)
print("Số lượng môn học:", so_luong_mon_hoc)
print("Mức lương tối thiểu:", MUC_LUONG_TOI_THIEU)

a = 17
b = 5
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)
diem = 6.5
tuoi = 20

# Kiểm tra điểm có đạt loại Khá (từ 6.5 đến dưới 8.0) hay không (kết hợp and)
kieu_kha = (diem >= 6.5) and (diem < 8.0)
print("Điểm đạt loại Khá:", kieu_kha)

# Kiểm tra tuổi có phải chưa đủ 18 hoặc trên 60 không (kết hợp or)
ngoai_do_tuoi = (tuoi < 18) or (tuoi > 60)
print("Chưa đủ 18 hoặc trên 60 tuổi:", ngoai_do_tuoi)

#P hủ định lại điều kiện trên bằng not
print("Phủ định điều kiện điểm Khá:", not kieu_kha)
print("Phủ định điều kiện tuổi:", not ngoai_do_tuoi)

x = 10

x += 5
print(x)

x -= 3
print(x)

x *= 2
print(x)

x /= 4
print(x)

x //= 2
print(x)

x **= 3
print(x)

danh_sach = [1, 2, 3, "python"]
print(3 in danh_sach)

list_1 = [1, 2, 3]
list_2 = list_1
print(list_2 is list_1)
print(2 + 3 * 4 ** 2)
print((2 + 3) * 4 ** 2)
print(10 > 5 and 3 < 1 or not False)

bien = 10
print(bien, type(bien))

bien = "Xin chao"
print(bien, type(bien))

bien = 3.14
print(bien, type(bien))

bien = True
print(bien, type(bien))

ho_ten = "Nguyen Van A"
diem_toan = 8.0
diem_ly = 7.5
diem_hoa = 9.0

dtb = (diem_toan + diem_ly + diem_hoa) / 3

la_gioi = dtb >= 8.0
la_kha = dtb >= 6.5 and dtb < 8.0
la_trung_binh = dtb >= 5.0 and dtb < 6.5
la_yeu = dtb < 5.0

print(ho_ten, "- DTB:", round(dtb, 2))
print("Dat loai Gioi?", la_gioi)
print("Dat loai Kha?", la_kha)
print("Dat loai Trung binh?", la_trung_binh)
print("Dat loai Yeu?", la_yeu)
print("Kieu du lieu cua la_gioi:", type(la_gioi))