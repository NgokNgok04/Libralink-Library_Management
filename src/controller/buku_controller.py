import sqlite3
from models.buku import *
from controller.peminjaman_controller import *
class Buku_Controller:
    def __init__(self):
        self.conn = sqlite3.connect("libralink.db")
        self.cursor = self.conn.cursor()
        self.peminjaman_controller = Peminjaman_Controller()

    def get_list_buku(self):
        daftar_buku = []
        self.cursor.execute('SELECT * FROM buku')
        rows = self.cursor.fetchall()

        for row in rows:
            buku = Buku(*row)
            daftar_buku.append(buku)
        return daftar_buku
    
    def get_filter_list_buku(self,search_query):
        self.cursor.execute("SELECT * FROM buku WHERE judul LIKE ?", ('%' + search_query + '%',))
        rows = self.cursor.fetchall()

        daftar_buku = []
        for row in rows:
            buku = Buku(*row)
            daftar_buku.append(buku)
        return daftar_buku
    
    def insert_buku(self, judul, kode, path)-> tuple[str,bool]:
        message = "Tambah buku gagal"
        if judul and kode and path:
            if len(kode) == 13 and kode.isdigit():
                self.cursor.execute("INSERT INTO buku (judul, isbn, path) VALUES (?, ?, ?)", (judul, kode, path))
                self.conn.commit()

                message = "Sukses menambahkan buku"
                return message,True
            else:
                message = "ISBN harus berupa 13 angka"
        else:
            message = "Harap melengkapi form"
        return message, False
    
    def edit_buku(self, judul, kode, path, buku_id)-> tuple[str,bool]:
        message = "Edit buku gagal"
        if judul and kode and path and buku_id:
            if len(kode) == 13 and kode.isdigit():
                if self.peminjaman_controller.isBukuBorrowed(buku_id):
                    message = "Tidak dapat mengedit buku yang sedang dipinjam."
                    return message, False
                self.cursor.execute("UPDATE buku SET judul = ?, isbn = ?, path = ? WHERE buku_id = ?", (judul, kode, path, buku_id))
                self.conn.commit()
                message = "Sukses mengedit buku"
                return message, True
            else:
                message = "ISBN harus berupa 13 angka"
        else:
            message = "Harap melengkapi form"

        return message, False

    def delete_buku(self,buku_id) -> tuple[str, bool]:
        message = "Gagal menghapus buku"
        if self.peminjaman_controller.isBukuBorrowed(buku_id):
            message = "Tidak dapat menghapus buku yang sedang dipinjam."
            return message, False

        self.cursor.execute('DELETE FROM buku WHERE buku_id = ?', (buku_id,))
        self.conn.commit()
        message = "Sukses menghapus buku"
        return message, True

    def isIDBukuValid(self,buku_id):
        self.cursor.execute('SELECT * FROM buku WHERE buku_id = ?', (buku_id,))
        return len(self.cursor.fetchall()) != 0
 
    def __del__(self):
        self.cursor.close()
        self.conn.close()