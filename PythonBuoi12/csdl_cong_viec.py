import sqlite3

TEN_FILE_CSDL = "cong_viec.db"

def ket_noi_csdl():
    return sqlite3.connect(TEN_FILE_CSDL)

def tao_bang_neu_chua_co():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("""
    CREATE TABLE IF NOT EXISTS cong_viec (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ten_cong_viec TEXT NOT NULL,
        muc_do TEXT NOT NULL,
        hoan_thanh INTEGER NOT NULL DEFAULT 0
    )
    """)
    ket_noi.commit()
    ket_noi.close()

def them_cong_viec(ten_cong_viec, muc_do):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute(
        "INSERT INTO cong_viec (ten_cong_viec, muc_do, hoan_thanh) VALUES (?, ?, 0)",
        (ten_cong_viec, muc_do)
    )
    ket_noi.commit()
    ket_noi.close()

def lay_toan_bo_cong_viec():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT id, ten_cong_viec, muc_do, hoan_thanh FROM cong_viec ORDER BY id")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua

def xoa_cong_viec(id_cv):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("DELETE FROM cong_viec WHERE id = ?", (id_cv,))
    ket_noi.commit()
    ket_noi.close()

def danh_dau_hoan_thanh(id_cv):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("UPDATE cong_viec SET hoan_thanh = 1 WHERE id = ?", (id_cv,))
    ket_noi.commit()
    ket_noi.close()

def thong_ke_theo_muc_do():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT muc_do, COUNT(*) FROM cong_viec GROUP BY muc_do")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua