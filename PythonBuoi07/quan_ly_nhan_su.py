
#1 – Khai báo dữ liệu ban đầu:
danh_sach_nhan_vien = [
    {"ma_nhan_vien": "101", "ho_ten": "Nguyen Van Anh", "phong_ban": "IT", "chuc_vu": "Developer", "luong_co_ban": 15000000},
    {"ma_nhan_vien": "102", "ho_ten": "Ho Le Minh Anh", "phong_ban": "HR", "chuc_vu": "Recruiter", "luong_co_ban": 12000000},
    {"ma_nhan_vien": "103", "ho_ten": "Nguyen Trung Kien", "phong_ban": "Ke Toan", "chuc_vu": "Accountant", "luong_co_ban": 14000000},
    {"ma_nhan_vien": "104", "ho_ten": "Le Minh Thuy ", "phong_ban": "IT", "chuc_vu": "Tester", "luong_co_ban": 13000000},
]
lich_su_quy_luong = []

#2 – Hàm hiển thị & tìm kiếm:
def hien_thi_danh_sach_nhan_vien():
    print("\n" + "=" * 85)
    print(f"{'Ma NV':<10}{'Ho va ten':<20}{'Phong ban':<15}{'Chuc vu':<15}{'Luong co ban':<15}")
    print("-" * 85)
    for nv in danh_sach_nhan_vien:
        print(f"{nv['ma_nhan_vien']:<10}{nv['ho_ten']:<20}{nv['phong_ban']:<15}{nv['chuc_vu']:<15}{nv['luong_co_ban']:>12,} VND")
    print("=" * 85)

def tim_nhan_vien_theo_ma(ma_nhan_vien):
    for nv in danh_sach_nhan_vien:
        if nv["ma_nhan_vien"] == ma_nhan_vien:
            return nv
    return None

def xem_nhan_vien_theo_phong_ban():
    phong_can_xem = input("Nhap ten phong ban can xem (IT/HR/Ke Toan...): ").strip().title()
    nv_phong = [nv for nv in danh_sach_nhan_vien if nv["phong_ban"].title() == phong_can_xem]
    if len(nv_phong) == 0:
        print(f"-> Khong co nhan vien nao trong phong ban {phong_can_xem}.")
        return
    print(f"\nNHAN VIEN PHONG {phong_can_xem.upper()}:")
    for nv in nv_phong:
        print(f" - {nv['ma_nhan_vien']} - {nv['ho_ten']} - {nv['chuc_vu']} - {nv['luong_co_ban']:,} VND")

#3 – Hàm thêm nhân viên, cập nhật thông tin, xóa nhân viên:
def them_nhan_vien(ma_nhan_vien, ho_ten, phong_ban, chuc_vu, luong_co_ban):
    if tim_nhan_vien_theo_ma(ma_nhan_vien) is not None:
        print(f"-> Ma nhan vien {ma_nhan_vien} da ton tai, khong the them.")
        return
    danh_sach_nhan_vien.append({
        "ma_nhan_vien": ma_nhan_vien,
        "ho_ten": ho_ten,
        "phong_ban": phong_ban,
        "chuc_vu": chuc_vu,
        "luong_co_ban": luong_co_ban
    })
    print(f"-> Da them nhan vien {ho_ten} ({ma_nhan_vien}) thanh cong.")

def cap_nhat_nhan_su(ma_nhan_vien, chuc_vu_moi, luong_moi):
    nv = tim_nhan_vien_theo_ma(ma_nhan_vien)
    if nv is None:
        print(f"-> Khong tim thay nhan vien {ma_nhan_vien}.")
        return
    nv["chuc_vu"] = chuc_vu_moi
    nv["luong_co_ban"] = luong_moi
    print(f"-> Cap nhat thong tin nhan vien {ma_nhan_vien} thanh cong.")

def xoa_nhan_vien(ma_nhan_vien):
    nv = tim_nhan_vien_theo_ma(ma_nhan_vien)
    if nv is None:
        print(f"-> Khong tim thay nhan vien {ma_nhan_vien}.")
        return
    danh_sach_nhan_vien.remove(nv)
    print(f"-> Da xoa nhan vien {ma_nhan_vien} khoi he thong.")

# Bước 4.4 – Hàm thống kê & hàm nhập số nguyên an toàn (dùng try-except):
def thong_ke_quy_luong():
    if len(danh_sach_nhan_vien) == 0:
        print("-> Chua co nhan vien nao trong he thong.")
        return
    tong_quy_luong = sum(nv["luong_co_ban"] for nv in danh_sach_nhan_vien)
    print("\nDANH SACH NHAN SU VA LUONG:")
    for nv in danh_sach_nhan_vien:
        print(f" - {nv['ma_nhan_vien']} - {nv['ho_ten']} ({nv['phong_ban']}): {nv['luong_co_ban']:,} VND")
    print(f"\n>>> TONG QUY LUONG CONG TY: {tong_quy_luong:,} VND")

def nhap_so_nguyen(loi_nhac):
    while True:
        try:
            return int(input(loi_nhac))
        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap lai mot so nguyen.")

#5 – Menu chính & vòng lặp chương trình:
def hien_thi_menu():
    print("\n===== QUAN LY NHAN SU CONG TY =====")
    print("1. Hien thi danh sach tat ca nhan vien")
    print("2. Xem nhan vien theo phong ban")
    print("3. Them nhan vien moi")
    print("4. Cap nhat thong tin nhan su")
    print("5. Xoa nhan vien (nghi viec)")
    print("6. Thong ke quy luong")
    print("0. Thoat chuong trinh")

def chay_chuong_trinh():
    while True:
        hien_thi_menu()
        lua_chon = input("Nhap lua chon cua ban: ").strip()

        if lua_chon == "1":
            hien_thi_danh_sach_nhan_vien()
        elif lua_chon == "2":
            xem_nhan_vien_theo_phong_ban()
        elif lua_chon == "3":
            ma_nv = input("Nhap ma nhan vien moi: ").strip().upper()
            ho_ten = input("Nhap ho ten nhan vien: ").strip().title()
            phong_ban = input("Nhap phong ban: ").strip().title()
            chuc_vu = input("Nhap chuc vu: ").strip().title()
            luong = nhap_so_nguyen("Nhap luong co ban: ")
            them_nhan_vien(ma_nv, ho_ten, phong_ban, chuc_vu, luong)
        elif lua_chon == "4":
            ma_nv = input("Nhap ma nhan vien can cap nhat: ").strip().upper()
            chuc_vu_moi = input("Nhap chuc vu moi: ").strip().title()
            luong_moi = nhap_so_nguyen("Nhap luong co ban moi: ")
            cap_nhat_nhan_su(ma_nv, chuc_vu_moi, luong_moi)
        elif lua_chon == "5":
            ma_nv = input("Nhap ma nhan vien can xoa: ").strip().upper()
            xoa_nhan_vien(ma_nv)
        elif lua_chon == "6":
            thong_ke_quy_luong()
        elif lua_chon == "0":
            print("Cam on da su dung chuong trinh. Tam biet!")
            break
        else:
            print("-> Lua chon khong hop le, vui long chon lai.")

if __name__ == "__main__":
    chay_chuong_trinh()
