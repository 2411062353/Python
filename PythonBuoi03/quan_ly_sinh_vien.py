# Hoạt động 6
danh_sach_sv = [(8.5, "An"), (7.0, "Binh"), (9.2, "Chi"), (6.5, "Dung")]

# 1. Thêm sinh viên mới
danh_sach_sv.append((8.0, "Em"))

# 2. Xóa một sinh viên (biết chính xác cả điểm và tên)
danh_sach_sv.remove((7.0, "Binh"))

# 3. Sửa điểm cho sinh viên ở vị trí xác định (ví dụ vị trí 0)
danh_sach_sv[0] = (9.0, danh_sach_sv[0][1])

# 4. Kiểm tra một sinh viên có trong danh sách hay không (dùng toán tử in)
print("Chi co trong danh sach khong?", (9.2, "Chi") in danh_sach_sv)

# 5. Sắp xếp theo điểm tăng dần (mặc định so sánh phần tử đầu tiên của tuple)
danh_sach_sv.sort()
print("\nDanh sach sau khi sap xep theo diem tang dan:")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")

# 6. Sắp xếp giảm dần
danh_sach_sv.sort(reverse=True)
print("\nDanh sach sau khi sap xep theo diem giam dan:")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")


