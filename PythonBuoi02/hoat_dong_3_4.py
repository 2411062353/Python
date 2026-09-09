#Baitap3.1
so_nguyen = 15
so_thuc = 4.2
so_phuc = 3 + 4j

print(type(so_nguyen), type(so_thuc), type(so_phuc))
print(float(so_nguyen))  # ep int -> float
print(int(so_thuc))      # ep float -> int (cat phan thap phan)

#Baitap3.2
a = -7
b = 2.6789
c, d = 17, 5

print(abs(a))         # Gia trị tuyet doi -> 7
print(round(b))       # Lam tron -> 3
print(round(b, 2))    # Lam tron 2 chu so thap phan -> 2.68
print(pow(c, 2))      # c mu 2 -> 289
print(divmod(c, d))   # Tra ve (thuong, du) -> (3, 2)

#Baitap3.3
import math

a, b, c = 1, -3, 2
delta = b ** 2 - 4 * a * c
x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)

print(f"Delta = {delta}")
print(f"Nghiem x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")

#Baitap4.1
cau = "Lap trinh Python rat thu vi"

# In ra chuoi dao nguoc
chuoi_dao_nguoc = cau[::-1]
print("Chuoi dao nguoc:", chuoi_dao_nguoc)

# Kiem tra palindrome
is_palindrome = cau == cau[::-1]
print("Co phai Palindrome khong?:", is_palindrome)

 #Baitap4.2
ten = "Nam"

# Thu gan lai mot ky tu se bao loi TypeError:
# ten[0] = "T"  # TypeError: 'str' object does not support item assignment

# Cach thay doi hop leBang cach tao chuoi moi:
ten_moi = "T" + ten[1:]
print(ten_moi)  # Ket qua: Tam

#Baitap4.3
cau = "  Toi dang HOC Python rat vui  "

print(cau.strip())                          # 'Toi dang HOC Python rat vui'
print(cau.strip().upper())                  # 'TOI DANG HOC PYTHON RAT VUI'
print(cau.strip().lower())                  # 'toi dang hoc python rat vui'
print(cau.strip().replace("HOC", "hoc"))    # 'Toi dang hoc Python rat vui'
print(cau.strip().split())                  # ['Toi', 'dang', 'HOC', 'Python', 'rat', 'vui']
print(len(cau.strip().split()))             # 6
print(cau.count("o"))                       # 1
print(cau.find("Python"))                   # 15
print(cau.strip().startswith("Toi"))        # True
print(cau.strip().endswith("vui"))          # True
print("-".join(["Python", "that", "thu", "vi"])) # 'Python-that-thu-vi'

#Baitap4.4
ho_ten_tho = "   nguyen   van   an  "
ho_ten_sach = " ".join(ho_ten_tho.split()).title()
print(ho_ten_sach) 
