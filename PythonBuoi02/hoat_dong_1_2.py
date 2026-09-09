#Baitap1.1
ho_ten = input("Nhap ho ten: ")
nam_sinh = int(input("Nhap nam sinh: "))
diem_tb = float(input("Nhap diem trung binh: "))

#Baitap1.2
print("Python", "la", "ngon", "ngu", "lap trinh", sep="-")
print("Dong 1", end=" | ")
print("Dong 2")

#Baitap1.3
ho_ten = "Ho Thu Hien"
nam_sinh = 2006
diem_tb = 8.5

# f-string (cách 1)
print(f"Ho ten: {ho_ten} - Nam sinh: {nam_sinh} - DTB: {diem_tb:.2f}")

# str.format(cách 2)
print("Ho ten: {} - Nam sinh: {} - DTB: {:.2f}".format(ho_ten, nam_sinh, diem_tb))

# Toán tử %(cách 3)
print("Ho ten: %s - Nam sinh: %d - DTB: %.2f" % (ho_ten, nam_sinh, diem_tb))

#Baitap2.1
# Chu thich mot dong: khai bao thong tin sinh vien
"""
Chu thich/docstring nhieu dong:
Chuong trinh quan ly diem sinh vien - Buoi 2
"""
ho_ten = "Tran Thi B"  # bien luu ho ten 

#Baitap2.2
s1 = 'Xin chao'
s2 = "Ban co khoe khong?"
s3 = '''Day la
mot chuoi
nhieu dong'''
s4 = "Duong dan: C:\\Python\\data"
s5 = r"Duong dan raw: C:\Python\data"
s6 = "Toi ten la \"Nam\", con ban ten gi?"

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)