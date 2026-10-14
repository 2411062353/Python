#1.1.Cửa sổ cơ bản
import tkinter as tk
cua_so=tk.Tk()
cua_so.title("Cua so Tkinter dau tien")
cua_so.geometry("400x300")     #rong x cao (don vi pixel)
cua_so.mainloop()   # vong lap su kien, giu cua so hien thi

#1.2.Tùy chỉnh không cho resize và thêm nội dung
import tkinter as tk
cua_so=tk.Tk()
cua_so.title("Ung dung demo")
cua_so.geometry("400x300")
cua_so.resizable(False, False)  #khong cho keo rong/cao
nhan=tk.Label(cua_so, text="Xin chao Tkinter!", font=("Arial", 16))
nhan.pack(pady=20)
cua_so.mainloop()

#2.Widget&Frame-khái niệm tổ chức giao diện
import tkinter as tk
cua_so=tk.Tk()
cua_so.title("Vi du Frame")
cua_so.geometry("400x300")
khung_tren=tk.Frame(cua_so,bg="lightblue",height=100)
khung_tren.pack(fill="x")
khung_duoi=tk.Frame(cua_so,bg="lightyellow")
khung_duoi.pack(fill="both",expand=True)
tk.Lable(khung_tren,text="Khu vuc tieu de", bg="lightblue").pack(pady=10)
tk.Lable(khung_duoi,text="Khu vuc noi dung", bg="lightyellow").pack(pady=10)
cua_so.mainloop()
