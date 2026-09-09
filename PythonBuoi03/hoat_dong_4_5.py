# 4.1 - Khai báo & tính bất biến:
toa_do = (3, 5)
print(toa_do, type(toa_do))

# 4.2 - Unpacking tuple: 
x, y = toa_do 
print("x =", x, "- y =", y) 
# Doi gia tri 2 bien bang unpacking (khong can bien tam) 
a, b = 10, 20 
a, b = b, a 
print("a =", a, "- b =", b)

# 4.3 - Trả về nhiều giá trị từ một biểu thức: 
c, d = 17, 5 
thuong_du = divmod(c, d) # divmod tra ve mot tuple (thuong, du) 
thuong, du = thuong_du # unpacking ket qua 
print(f"{c} chia {d} duoc thuong {thuong}, du {du}")

# 5: Vận dụng Tuple - Tọa độ điểm & khoảng cách
import math 
diem_a = (2, 3)
diem_b = (7, 8)

xa, ya = diem_a
xb, yb = diem_b

khoang_cach = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
print(f"Khoang cach giua {diem_a} va {diem_b} la: {round(khoang_cach, 2)}")
# Tạo thêm danh sách các điểm và tính khoảng cách tới gốc tọa độ (0, 0)
cac_diem = [(0, 0), (3, 4), (6, 8)]

print("\n--- Khoảng cách từ từng điểm tới gốc tọa độ (0, 0) ---")
for x, y in cac_diem:
    kc = math.sqrt(x**2 + y**2)
    print(f"Khoang cach tu diem ({x}, {y}) den goc to a do (0,0) la: {round(kc, 2)}")