import tkinter as tk

def nhap_vao(value):
    hien_thi.insert(tk.END, value)

def xoa_man_hinh():
    hien_thi.delete(0, tk.END)

def tinh_ket_qua():
    try:
        bieu_thuc = hien_thi.get()
        ket_qua = str(eval(bieu_thuc))
        hien_thi.delete(0, tk.END)
        hien_thi.insert(0, ket_qua)
    except Exception:
        hien_thi.delete(0, tk.END)
        hien_thi.insert(0, "Lỗi")

cua_so = tk.Tk()
cua_so.title("Máy tính bỏ túi")
cua_so.geometry("300x400")
cua_so.resizable(False, False)

hien_thi = tk.Entry(cua_so, font=("Arial", 20), justify="right", bd=5)
hien_thi.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(cua_so, text=text, font=("Arial", 14), bg="lightgreen", command=tinh_ket_qua)
    else:
        btn = tk.Button(cua_so, text=text, font=("Arial", 14), command=lambda t=text: nhap_vao(t))
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

btn_c = tk.Button(cua_so, text="C", font=("Arial", 14), bg="lightcoral", command=xoa_man_hinh)
btn_c.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

for i in range(6):
    cua_so.grid_rowconfigure(i, weight=1)
for i in range(4):
    cua_so.grid_columnconfigure(i, weight=1)

cua_so.mainloop()