import sqlite3
import re
from models.anggota import *
from controller.peminjaman_controller import *

db_folder = os.path.join(os.path.dirname(__file__), '../database')
os.makedirs(db_folder, exist_ok=True)
db_path = os.path.join(db_folder, 'libralink.db')

class Anggota_Controller:
    def __init__(self):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.peminjaman_controller = Peminjaman_Controller()

    def get_list_anggota(self):
        daftar_anggota = []
        self.cursor.execute('SELECT * FROM anggota')
        rows = self.cursor.fetchall()

        for row in rows:
            anggota = Anggota(*row)
            daftar_anggota.append(anggota)

        return daftar_anggota

    def insert_anggota(self, nama, email, telepon, status) -> tuple[str,bool]:
        message = "Gagal menambahkan anggota"
        if nama and email and telepon and status is not None:
            if re.match(r"[^@]+@[^@]+\.[^@]+", email):  # Check email format
                if re.match(r"^08\d{9,11}$", telepon):  # Check telephone pattern
                    self.cursor.execute("INSERT INTO anggota (nama, email, telephone, status_anggota) VALUES (?, ?, ?, ?)", (nama, email, telepon, status))
                    self.conn.commit()

                    message = "Sukses menambahkan anggota"
                    return message,True
                else:
                    message = "Nomor telepon haris diawali '08' dan memiliki 11 - 13 digit"
            else:
                message = "Format email harus berupa %@%.%"
        else:
            message = "Harap melengkapi form"
        return message, False

    def edit_anggota(self, nama, email, telepon, status, anggota_id) -> tuple[str, bool]:
        message = "Gagal mengedit anggota"
        if nama and email and telepon and status is not None:
            if re.match(r"[^@]+@[^@]+\.[^@]+", email):  # Check email format
                if re.match(r"^08\d{9,11}$", telepon):  # Check telephone pattern
                    if status:
                        if self.peminjaman_controller.isAnggotaBorrow(anggota_id):
                            message = "Tidak dapat menonaktifkan anggota yang memiliki peminjaman buku."
                            return message,False
                    self.cursor.execute("UPDATE anggota SET nama = ?, email = ?, telephone = ?, status_anggota = ? WHERE anggota_id = ?", (nama, email, telepon, status, anggota_id))
                    self.conn.commit()
                    message = "Sukses mengedit anggota"
                    return message,True
                else:
                    message = "Nomor telepon haris diawali '08' dan memiliki 11 - 13 digit"
            else:
                message = "Format email harus berupa %@%.%"
        else:
            message = "Harap melengkapi form"
    
        return message,False
    
    def get_list_filter_anggota(self,search_query):
        self.cursor.execute('SELECT * FROM anggota WHERE nama LIKE ?', ('%' + search_query + '%',))
        rows = self.cursor.fetchall()
        
        daftar_anggota = []
        for row in rows:
            anggota = Anggota(*row)
            daftar_anggota.append(anggota)
        
        return daftar_anggota
    
    def delete_anggota(self,anggota_id) -> tuple[str, bool]:
        message = "Gagal menghapus anggota"
        if self.peminjaman_controller.isAnggotaBorrow(anggota_id):
            message = "Tidak dapat menghapus anggota yang memiliki peminjaman buku."
            return message, False
    
        self.cursor.execute('DELETE FROM anggota WHERE anggota_id = ?', (anggota_id,))
        self.conn.commit()
        message = "Sukses menghapus anggota"
        return message, True

    def __del__(self):
        self.cursor.close()
        self.conn.close()