import csdl_cong_viec as db

# 1. Tạo bảng cơ sở dữ liệu
db.tao_bang_neu_chua_co()

# 2. Thêm 4 công việc mẫu
db.them_cong_viec("Hoan thanh Lab12", "Quan trọng")
db.them_cong_viec("Hoc tu vung tieng Trung", "Bình thường")
db.them_cong_viec("Don dep phong lam việc", "Thấp")
db.them_cong_viec("Nop bai tap lon KTXLAVT", "Khẩn cấp")

print("--- DANH SACH CONG VIEC BAN DAU ---")
for cv in db.lay_toan_bo_cong_viec():
    print(cv)

# 3. Đánh dấu hoàn thành cho công việc có id = 1
db.danh_dau_hoan_thanh(1)
print("\n--- SAU KHI DANH DAU HOAN THANH id=1 ---")
for cv in db.lay_toan_bo_cong_viec():
    print(cv)

# 4. Xóa công việc có id = 3
db.xoa_cong_viec(3)
print("\n--- SAU KHI XOA id=3 ---")
for cv in db.lay_toan_bo_cong_viec():
    print(cv)

# 5. Thống kê số lượng công việc theo mức độ
print("\n--- THONG KE THEO MUC DO ---")
print(db.thong_ke_theo_muc_do())