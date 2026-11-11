import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import csdl_cong_viec as db

DANH_SACH_MUC_DO = ["Quan trọng", "Bình thường", "Khẩn cấp", "Thấp"]

class UngDungCongViec(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quan ly Cong viec ca nhan")
        self.geometry("560x480")
        self.resizable(False, False)
        db.tao_bang_neu_chua_co()
        self.khoi_tao_giao_dien()
        self.tai_lai_danh_sach()

    def khoi_tao_giao_dien(self):
        khung_nhap = tk.Frame(self)
        khung_nhap.pack(pady=10, padx=10, fill="x")

        tk.Label(khung_nhap, text="Tên công việc:").grid(row=0, column=0, sticky="w", pady=5)
        self.o_nhap_ten = tk.Entry(khung_nhap, width=30)
        self.o_nhap_ten.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Mức độ:").grid(row=1, column=0, sticky="w", pady=5)
        self.chon_muc_do = ttk.Combobox(khung_nhap, values=DANH_SACH_MUC_DO, width=27, state="readonly")
        self.chon_muc_do.current(0)
        self.chon_muc_do.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(khung_nhap, text="Thêm công việc", command=self.xu_ly_them).grid(row=2, column=0, columnspan=2, pady=10)

        khung_danh_sach = tk.Frame(self)
        khung_danh_sach.pack(pady=5, padx=10, fill="both", expand=True)

        self.listbox_cv = tk.Listbox(khung_danh_sach, width=75, height=14)
        self.listbox_cv.pack(side="left", fill="both", expand=True)

        thanh_cuon = tk.Scrollbar(khung_danh_sach, orient="vertical", command=self.listbox_cv.yview)
        thanh_cuon.pack(side="right", fill="y")
        self.listbox_cv.config(yscrollcommand=thanh_cuon.set)

        khung_nut = tk.Frame(self)
        khung_nut.pack(pady=10)

        tk.Button(khung_nut, text="Đánh dấu hoàn thành", command=self.xu_ly_hoan_thanh).grid(row=0, column=0, padx=5)
        tk.Button(khung_nut, text="Xóa công việc", command=self.xu_ly_xoa).grid(row=0, column=1, padx=5)
        tk.Button(khung_nut, text="Thống kê theo mức độ", command=self.xu_ly_thong_ke).grid(row=0, column=2, padx=5)

    def tai_lai_danh_sach(self):
        self.listbox_cv.delete(0, tk.END)
        self.danh_sach_hien_tai = db.lay_toan_bo_cong_viec()
        for cv in self.danh_sach_hien_tai:
            id_cv, ten_cv, muc_do, hoan_thanh = cv
            trang_thai = "[Đã xong]" if hoan_thanh == 1 else "[Chưa xong]"
            self.listbox_cv.insert(tk.END, f"{trang_thai} {ten_cv} - Mức độ: {muc_do}")

    def xu_ly_them(self):
        ten_cv = self.o_nhap_ten.get().strip()
        muc_do = self.chon_muc_do.get()
        if ten_cv == "":
            messagebox.showerror("Lỗi", "Vui lòng nhập tên công việc.")
            return
        db.them_cong_viec(ten_cv, muc_do)
        self.o_nhap_ten.delete(0, tk.END)
        self.tai_lai_danh_sach()
        messagebox.showinfo("Thành công", f"Đã thêm: {ten_cv}")

    def xu_ly_xoa(self):
        lua_chon = self.listbox_cv.curselection()
        if not lua_chon:
            messagebox.showerror("Lỗi", "Vui lòng chọn một công việc để xóa.")
            return
        id_cv = self.danh_sach_hien_tai[lua_chon[0]][0]
        db.xoa_cong_viec(id_cv)
        self.tai_lai_danh_sach()

    def xu_ly_hoan_thanh(self):
        lua_chon = self.listbox_cv.curselection()
        if not lua_chon:
            messagebox.showerror("Lỗi", "Vui lòng chọn một công việc để đánh dấu hoàn thành.")
            return
        id_cv = self.danh_sach_hien_tai[lua_chon[0]][0]
        db.danh_dau_hoan_thanh(id_cv)
        self.tai_lai_danh_sach()

    def xu_ly_thong_ke(self):
        du_lieu = db.thong_ke_theo_muc_do()
        if not du_lieu:
            messagebox.showinfo("Thông báo", "Chưa có dữ liệu để thống kê.")
            return
        muc_do_lst = [dong[0] for dong in du_lieu]
        so_luong_lst = [dong[1] for dong in du_lieu]

        plt.figure(figsize=(6, 4))
        plt.bar(muc_do_lst, so_luong_lst, color="seagreen")
        plt.title("Thống kê công việc theo mức độ")
        plt.xlabel("Mức độ")
        plt.ylabel("Số lượng")
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    app = UngDungCongViec()
    app.mainloop()