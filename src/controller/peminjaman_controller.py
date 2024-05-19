import sqlite3
import os
from dateutil import parser
from datetime import datetime
from models.peminjaman import *
# from controller.buku_controller import Buku_Controller

db_folder = os.path.join(os.path.dirname(__file__), '../database')
os.makedirs(db_folder, exist_ok=True)
db_path = os.path.join(db_folder, 'libralink.db')

class Peminjaman_Controller:
    def __init__(self):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        # self.buku_controller = Buku_Controller()

    def get_list_peminjaman(self,anggota_id):
        daftar_peminjaman = []
        self.cursor.execute('SELECT * FROM peminjaman WHERE anggota_id = ?',(anggota_id,))
        rows = self.cursor.fetchall()

        for row in rows:
            peminjaman = Peminjaman(*row)
            self.cursor.execute('SELECT judul FROM buku WHERE buku_id = ?',(row[1],))
            title = self.cursor.fetchall()
            peminjaman.addTitle(title)
            daftar_peminjaman.append(peminjaman)

        return daftar_peminjaman

    def insert_peminjaman(self, buku_id, tanggal_pinjam, tanggal_pengembalian, anggota_id)->tuple[str,bool]:
        buku_id = str(buku_id)
        
        self.cursor.execute('SELECT * FROM buku WHERE buku_id = ?', (buku_id,))

        isValidIDBuku = len(self.cursor.fetchall()) != 0
        isCanBorrow = self.isAnggotaCanBorrow(anggota_id)
        isBukuBorrowed = self.isBukuBorrowed(buku_id)
        isDateValid = self.isDateValid(tanggal_pengembalian,tanggal_pinjam)

        if (isValidIDBuku and isCanBorrow and (not isBukuBorrowed) and isDateValid):
            self.cursor.execute("INSERT INTO peminjaman (anggota_id, buku_id, tanggal_pinjam, tanggal_pengembalian ) VALUES (?,?,?,?)",(anggota_id,buku_id,tanggal_pinjam,tanggal_pengembalian))
            self.conn.commit()
            message = "Tambah Peminjaman Berhasil"
            return message,True
        else:
            if not buku_id:
                message = "Harap melengkapi form"
            elif not buku_id.isdigit():
                message = "ID Buku harus berupa angka"
            elif not isValidIDBuku:
                message = "ID Buku tidak ada pada daftar buku"
            elif not isCanBorrow:
                message = "Anggota sudah melebihi batas maksimal peminjaman"
            elif isBukuBorrowed:
                message = "Buku sedang dipinjam anggota lain"
            elif not isDateValid:
                message = "Pastikan tanggal pengembalian setelah tanggal peminjaman"
            
            
            return message, False
        
    def delete_peminjaman(self,buku_id):
        self.cursor.execute('SELECT anggota_id FROM peminjaman WHERE buku_id = ?', (buku_id,))
        anggotaToShow = self.cursor.fetchall()
        anggotaToShow = anggotaToShow[0][0]
        self.cursor.execute('DELETE FROM peminjaman WHERE buku_id = ?', (buku_id,))
        self.conn.commit()
        return anggotaToShow

    def isBukuBorrowed(self,buku_id):
        self.cursor.execute("SELECT * FROM peminjaman WHERE buku_id = ?", (buku_id,))
        result = self.cursor.fetchone()
        if not result:
            return False
        else:
            return True

    def isAnggotaCanBorrow(self,anggota_id):
        self.cursor.execute('SELECT * FROM peminjaman WHERE anggota_id = ?', (anggota_id,))
        nBorrowedBook = len(self.cursor.fetchall())
        return (nBorrowedBook < 3)

    def isAnggotaBorrow(self,anggota_id):
        self.cursor.execute("SELECT * FROM peminjaman WHERE anggota_id = ?", (anggota_id,))
        return len(self.cursor.fetchall()) != 0

    def isDateValid(self,date_after,date_before):

        outputTanggal = "%Y-%m-%d"
        date_format = "%Y-%m-%d"

        date_after = datetime.strptime(parser.parse(date_after).strftime(outputTanggal), date_format)
        date_before = datetime.strptime(parser.parse(date_before).strftime(outputTanggal), date_format)
        
        return date_after > date_before


    def __del__(self):
        self.cursor.close()
        self.conn.close()